import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime import *
from openpyxl import Workbook
import getpass
import functions
from functions import *
from GetData import *


def betweenDates():
    delay = 3

    init_year = int (input ("input initial year (yyyy) : "))
    init_month = int (input ("input initial month (MM) : "))
    init_day = int (input ("input initial day (dd) : "))
    init_date = datetime.datetime(init_year, init_month, init_day)
    final_year = int (input ("input finish year (yyyy) : "))
    final_month = int (input ("input finish month (MM) : "))
    final_day = int (input ("input finish day (dd) : "))
    final_date = datetime.datetime(final_year, final_month, final_day)
    delta = final_date - init_date
    delta = delta.days + 1

    fileName = str(date(init_year,init_month,init_day)) + '--' + str(date(final_year,final_month,final_day)) + '.xlsx'
    fileName = str(fileName)
    wb = Workbook()
    ws = wb.active
    wb.save(filename = fileName)

    username = input("Enter Gameiom username: ")
    password = getpass.getpass("Password: ") #privately gets password (only in terminal, doesn't work on IDEs)

    cDriverpath = str(os.path.dirname(os.path.abspath(__file__)))+ '/chromedriver'

    driver = webdriver.Chrome(cDriverpath)

    driver.get('https://cdn.gameiom.com/gameiom/backoffice/production/latest/index.html#dailyReport')


    GameiomLogin(username, password, driver, delay)
    time.sleep(2)
    if (LoginError(driver) == True):
            driver.quit()
            return 0
    else:
        print("Login Successful")

    xpath_day = gotoDate(driver, init_year, init_month, init_day)
    day = init_day
    time.sleep(2)
    date = date(init_year,init_month,init_day)
    tDelta = timedelta(days=1)

    downloadsPath = getPath('Downloads')
    downloadsPath_W_CSV = str(downloadsPath + '/gm-dailyReport.csv')


    for i in range(delta):
        
        try:
            elem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/div/div/portable-export/div/button[2]')))#driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/portable-export/div/button[2]')
            elem.click()
        except TimeoutException:
            print("Error 02")
     
        while not os.path.exists(downloadsPath_W_CSV):
            time.sleep(1)
        moveData(date, fileName, downloadsPath_W_CSV)
        date += tDelta
        
        if ((i+1)== delta):
            break
        nextDay(day,driver)
        day = day + 1
        time.sleep(1)

    driver.quit()
    return 0

betweenDates()


