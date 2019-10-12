import selenium
from selenium import webdriver
from selenium.webdriver import Chrome
from pyvirtualdisplay import Display
from selenium.webdriver.common.keys import Keys

import time
import json
import datetime
import hashlib

from insertdatabase import InsertDB



def parse_google(htmlstring, driver, f):
    table_name = "ncaa"
    currentDT = datetime.datetime.now()
    
    print("///---------Google Search--------------///")
    with open('ncaa_flashscore.json') as json_file:
        items = json.load(json_file)
        counts = len(items)
        count = 1

        for item in items:
            data_base = []
            event_time = item['event-time']
            home_team = item['home-name']
            home_score = item['home-score']
            away_team = item['away-name']
            away_score = item['away-score']

            print(home_team, " v ", away_team, "-------------", count)
            search_key = home_team + " v " + away_team
            
            search_google = driver.find_element_by_xpath("//input[contains(@class, 'gLFyf') and contains(@class, 'gsfi')]")
                
            search_google.send_keys(search_key)
            search_google.send_keys(Keys.ENTER)
            time.sleep(5)
            
            try:
                teamNames = driver.find_elements_by_xpath("//div[contains(@class, 'liveresults-sports-immersive__team-name-width')]")

                fstName = teamNames[0].text
                sndName = teamNames[1].text

                fstScore = driver.find_element_by_xpath("//div[contains(@class, 'imso_mh__l-tm-sc')]").text
                sndScore = driver.find_element_by_xpath("//div[contains(@class, 'imso_mh__r-tm-sc')]").text

                print(fstName, "<----->", fstScore)
                print(sndName, "<----->", sndScore)
                
                if (home_team in fstName and home_score == fstScore) and (away_team in sndName and away_score == sndScore):
                    googleMatch = "True"
                elif (away_team in fstName and away_score == fstScore) and (home_team in sndName and home_score == sndScore):
                    googleMatch = "True"
                else:
                    googleMatch = "False"
            except:
                try:
                    teamNames = driver.find_elements_by_xpath("//td[contains(@class, 'liveresults-sports-immersive__match-grid-right-border')]//div[contains(@class, 'ellipsisize') and contains(@class, 'kno-fb-ctx')]/span")

                    fstName = teamNames[0].text
                    sndName = teamNames[1].text

                    teamScores = driver.find_elements_by_xpath("//td[contains(@class, 'liveresults-sports-immersive__match-grid-right-border')]//div[@class='imspo_mt__tt-w']")

                    fstScore = teamScores[0].text
                    sndScore = teamScores[1].text

                    print(fstName, "<----->", fstScore)
                    print(sndName, "<----->", sndScore)
                    
                    if (fstName in home_team and home_score == fstScore) and (sndName in away_team and away_score == sndScore):
                        googleMatch = "True"
                    elif (fstName in away_team and away_score == fstScore) and (sndName in home_team and home_score == sndScore):
                        googleMatch = "True"
                    else:
                        googleMatch = "False"
                except:
                    googleMatch = "False"

            try:
                gameStatus = driver.find_element_by_xpath("//span[contains(@class, 'imso_mh__ft-mtch') and contains(@class, 'imso-medium-font')]").text
            except:
                gameStatus = "Not"

            if "final" in gameStatus.lower():
                game_status = "Final"
            else :
                game_status = "Future"
                
            create_time = str(datetime.datetime.now())
            update_time = ""
            print("---------------------------?????", event_time + home_team + away_team)

            string_id = event_time + home_team + away_team
            m = hashlib.md5()
            m.update(string_id.encode('utf8'))
            identifier = m.hexdigest()
            print("hash-------------------->", identifier)

            insertdb = InsertDB()
            data_base.append((event_time,
                            home_team,
                            home_score,
                            away_team,
                            away_score,
                            googleMatch,
                            game_status,
                            identifier,
                            create_time,
                            update_time))

            insertdb.insert_document(data_base, table_name)

            info = {
                "event-time": event_time,
                "home-name" : home_team,
                "home-score" : home_score,
                "away-name" : away_team,
                "away-score" : away_score,
                "google-matching" : googleMatch,
                "game-status" : game_status,
                "indentifier" : identifier,
                "create-time" : create_time,
                "update-time" : update_time
            }

            json.dump(info, f)
            if count != counts:
                f.write(',\n')          

            search_google1 = driver.find_element_by_xpath("//input[contains(@class, 'gLFyf') and contains(@class, 'gsfi')]")
            search_google1.clear()

            count += 1
            # return
    driver.close()
    driver.quit()




display = Display(visible=0, size=(800, 600))
display.start()

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--headless')

path = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(executable_path=path, options=options)

driver.get("https://www.google.com/")
time.sleep(2)

with open("ncaa_google.json", "w", encoding='utf8') as f:
    f.write('[\n')
    parse_google(driver.page_source, driver, f)
    f.write(']\n')
    f.close()

    display.stop()
    