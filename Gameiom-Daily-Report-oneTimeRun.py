import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
from openpyxl import Workbook
from datetime import date, timedelta
from datetime import datetime
import getpass
import sys
from src import GetData as gd
from src import functions as f
from openpyxl import Workbook
import os

def oneRun(username, password):
    delay = 3

    try:
        init_year = int (input ("input initial year (yyyy) : "))
        init_month = int (input ("input initial month (MM) : "))
        init_day = int (input ("input initial day (dd) : "))
        init_date = date(init_year, init_month, init_day)
        
    except ValueError:
        print('Error Try again')
    final_date = date.today()
    delta = final_date - init_date
    delta = delta.days + 1

    dest_filename = 'data.xlsx'
    fileName = str(os.path.dirname(os.path.abspath(__file__)))+'/data'
    if not fileName:
        wb = Workbook()
        wb.save(str(fileName+'/'+dest_filename))
    fileName = str(fileName+'/'+dest_filename)
    #username = input("Enter Gameiom username: ")
    #password = getpass.getpass("Password: ") #privately gets password (only in terminal, doesn't work on IDEs)

    cDriverpath = str(os.path.dirname(os.path.abspath(__file__)))+ '/src/chromedriver'

    driver = webdriver.Chrome(cDriverpath)

    driver.get('https://cdn.gameiom.com/gameiom/backoffice/production/latest/index.html#dailyReport')


    f.GameiomLogin(username, password, driver, delay)
    time.sleep(2)
    if (f.LoginError(driver) == True):
            driver.quit()
            return 0
    else:
        print("Login Successful")

    f.gotoDate(driver, init_year, init_month, init_day)
    time.sleep(2)
    date1 = date(init_year,init_month,init_day)
    tDelta = timedelta(days=1)

    downloadsPath = f.getPath('Downloads')
    downloadsPath_W_CSV = str(downloadsPath + '/gm-dailyReport.csv')


    for i in range(delta):
        
        try:
            elem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/div/div/portable-export/div/button[2]')))
            elem.click()
        except TimeoutException:
            print("Error 02")
     
        while not os.path.exists(downloadsPath_W_CSV):
            time.sleep(1)
        gd.moveData(date1, fileName, downloadsPath_W_CSV)
        date1 += tDelta
        
        if ((i+1)== delta):
            break
        f.nextDay(date1.day,driver)
        time.sleep(1)

    driver.quit()
username = str(sys.argv[1])
password = str(sys.argv[2])
oneRun(username, password)
