import time
from openpyxl import Workbook
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import getpass
from datetime import date, timedelta
from src import functions as f
from src import GetData as gd
from datetime import datetime
import os
import sys
import schedule

def prevDayCollect(username, password):
    delta = timedelta(days = 1)
    downloadsPath = f.getPath('Downloads')
    downloadsPath_W_CSV = str(downloadsPath + '/gm-dailyReport.csv')

    #username = input("Enter Gameiom username: ")
    #password = getpass.getpass("Password: ") #privately gets password (only in terminal, doesn't work on IDEs)

    cDriverpath = str(os.path.dirname(os.path.abspath(__file__)))+ '/src/chromedriver'

    driver = webdriver.Chrome(cDriverpath)
    driver.get('https://cdn.gameiom.com/gameiom/backoffice/production/latest/index.html#dailyReport')
    delay = 3
    f.GameiomLogin(username, password, driver, delay)
    time.sleep(2)

    if (f.LoginError(driver) == True):
        driver.quit()
        return 0
    else:
        print("Login Successful")


    f.prevDay(date.today().day, driver)

    dest_filename = 'data.xlsx'
    fileName = str(os.path.dirname(os.path.abspath(__file__)))+'/data'
    if not fileName:
        wb = Workbook()
        wb.save(fileName)
        
    file = fileName+'/'+dest_filename

    try:
        elem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/div/div/portable-export/div/button[2]')))
        elem.click()
    except TimeoutException:
        print("Error 02")
        driver.quit()

    gd.moveData((date.today() - delta), file, downloadsPath_W_CSV)


    driver.quit()
    return 0



username = str(sys.argv[1])
password = str(sys.argv[2])
prevDayCollect(username, password)
'''schedule.every().day.at("04:00").do(prevDayCollect)
while True:
    schedule.run_pending()
    time.sleep(1)'''
