import selenium
from selenium import webdriver
from selenium.webdriver import Chrome
from pyvirtualdisplay import Display
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import csv
import time
import random
import json



def parse_page(htmlstring, driver, f):
    time.sleep(5)
    print("//--------Scrapy Start-------------//")
    
    while True:
        try:
            moreBtn = driver.find_element_by_xpath("//a[contains(@class, 'event__more') and contains(@class, 'event__more--static')]")
            # moreBtn.click()
            print("---------------------------%%%%%%%%%%%%%%%%%%%%---------", moreBtn)
            time.sleep(5)
        except:
            print("----------------------------------No Button----------------")
            break
            
        try:
            driver.execute_script("arguments[0].click();", moreBtn)
            time.sleep(5)
        except:
            break

    current_year = driver.find_element_by_xpath("//div[contains(@class, 'teamHeader__text')]").text

    Items = driver.find_elements_by_xpath("//div[contains(@class, 'event__match') and contains(@class, 'event__match--static') and contains(@class, 'event__match--twoLine')]")

    eventTimes = driver.find_elements_by_xpath("//div[@class='event__time']")

    hometeamNames = driver.find_elements_by_xpath("//div[contains(@class, 'event__participant') and contains(@class, 'event__participant--home')]")

    awayteamNames = driver.find_elements_by_xpath("//div[contains(@class, 'event__participant') and contains(@class, 'event__participant--away')]")

    homeScores = driver.find_elements_by_xpath("//div[contains(@class, 'event__score') and contains(@class, 'event__score--home')]")

    awayScores = driver.find_elements_by_xpath("//div[contains(@class, 'event__score') and contains(@class, 'event__score--away')]")

    counts = len(Items)
    count = 1

    for eventTime, hometeamName, awayteamName, homeScore, awayScore in zip(eventTimes, hometeamNames, awayteamNames, homeScores, awayScores):
        
        event_time = current_year + "." +  eventTime.text 
        home_name = hometeamName.text
        away_name = awayteamName.text
        home_score = homeScore.text
        away_score = awayScore.text
        google_matching = ""

        print("-----------------", count, "--", counts)
        print("Event Time------------------------> : ", event_time)
        print("Home Name-------------------------> : ", home_name)
        print("Away Name-------------------------> : ", away_name)
        print("Home Score------------------------> : ", home_score)
        print("Away Score------------------------> : ", away_score)

        info = {
            "event-time": event_time,
            "home-name" : home_name,
            "home-score" : home_score,
            "away-name" : away_name,
            "away-score" : away_score,
            "google-matching" : google_matching,
            "game-status" : ""
        }

        
        json.dump(info, f)
        if count != counts:
            f.write(',\n')
        count += 1
    


display = Display(visible=0, size=(800, 600))
display.start()

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--headless')

path = "/usr/local/bin/chromedriver"

driver = webdriver.Chrome(executable_path=path, options=options)
driver.get("https://www.flashscore.com/american-football/usa/nfl/results/")
time.sleep(5)


with open("nfl_flashscore.json", "w", encoding='utf8') as f:
    f.write('[\n')
    parse_page(driver.page_source, driver, f)
    f.write(']\n')
    f.close()
    display.stop()
    driver.close()
    driver.quit()
    