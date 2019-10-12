import mysql.connector
import datetime

class InsertDB:

    mydb_name = "sportscore_db"

    def insert_document(self, documents, table_name):
        
        #****************** SERVER *****************#

        # mydb = mysql.connector.connect(
        #     user = "root",
        #     password = "Scraping1!",
        #     host = "35.197.51.164"
        # )
        mydb = mysql.connector.connect(
            user = "root",
            password = "rootsportsitescrapingapi",
            host = "localhost"
        )
        # print(mydb)

        mycursor = mydb.cursor()

        mycursor.execute("CREATE DATABASE IF NOT EXISTS " + self.mydb_name + " CHARACTER SET utf8 COLLATE utf8_general_ci")

        # ************** SERVER ********************* #
        # mydb = mysql.connector.connect(
        #     user = "root",
        #     password = "Scraping1!",
        #     host = "35.197.51.164",
        #     database = "poulsbo_db"
        # )
        mydb = mysql.connector.connect(
            user = "root",
            password = "rootsportsitescrapingapi",
            host = "localhost",
            database = self.mydb_name
        )
        # print("1------------", mydb)
        

        documents = documents[0]
        print(documents)

        mycursor = mydb.cursor()

        stmt = "SHOW TABLES LIKE '{}'".format(table_name)
        mycursor.execute(stmt)
        result = mycursor.fetchone()    

        if not result:
            sql = "CREATE TABLE {} (id INT(11) UNSIGNED AUTO_INCREMENT PRIMARY KEY, EventTime VARCHAR(50), HomeName VARCHAR(30), HomeScore VARCHAR(30), AwayName VARCHAR(30), AwayScore VARCHAR(30), GoogleMatch VARCHAR(10), GameStatus VARCHAR(15), Identifier VARCHAR(100), Created_Time VARCHAR(30), Updated_Time VARCHAR(30), INDEX (Identifier))".format(table_name)

            mycursor.execute(sql)
            mydb.commit()

        sql = "SELECT Identifier FROM {0} WHERE Identifier='{1}'".format(table_name, documents[7])
        mycursor.execute(sql)
        identifier_result = mycursor.fetchone()

        if not identifier_result:
            insert_sql = """INSERT INTO {} (EventTime, HomeName, HomeScore, AwayName, AwayScore, GoogleMatch, GameStatus, Identifier, Created_Time, Updated_Time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""".format(table_name)

            mycursor.execute(insert_sql, documents)
            mydb.commit()    
        
        else:
            update_sql = 'UPDATE {0} SET EventTime="{1}", HomeName="{2}", HomeScore="{3}", AwayName="{4}", AwayScore="{5}", GoogleMatch="{6}", GameStatus="{7}",  Updated_Time="{8}" WHERE Identifier="{9}"'.format(table_name, documents[0], documents[1], documents[2], documents[3], documents[4], documents[5], documents[6], datetime.datetime.now(), documents[7])    

            mycursor.execute(update_sql)
            mydb.commit()

        

        print("==================> Now time:", datetime.datetime.now())

