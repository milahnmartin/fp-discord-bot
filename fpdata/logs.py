from fpdata.constants import *
import mysql.connector
from datetime import date

mydb = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USERNAME,
    password=MYSQL_PASSW,
    database=MYSQL_DB
)

mycursor = mydb.cursor()


def create_log_sql(pUser:str,pCommand:str,pTarget:str) -> None:
    current_time = date.today()
    global mycursor
    query = "INSERT INTO `fp-discord-bot`(`discord_username`,`command_used`,`player_target`)VALUES(%s,%s,%s);"
    parameters = (pUser,pCommand,pTarget)
    mycursor.execute(query,parameters)
    mydb.commit()
    print("[RECORD WAS CREATED] -> ",current_time)


def create_log_webhook(pUser:str,pCommand:str,pTarget:str) -> None:
    pass

