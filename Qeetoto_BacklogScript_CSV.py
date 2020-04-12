import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
from datetime import timedelta,date
import getpass
import functions
from functions import *
from GetData import *
from openpyxl import Workbook


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



username = input("Enter Gameiom username: ")
password = getpass.getpass("Password: ") #privately gets password (only in terminal, doesn't work on IDEs)


driver = webdriver.Chrome('/Users/macbookpro/Documents/Qeetoto Scripts/chromedriver')

driver.get('https://cdn.gameiom.com/gameiom/backoffice/production/latest/index.html#dailyReport')


try:
    elem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div/form/div[1]/input')))#driver.find_element_by_xpath('/html/body/div/div/div/div/form/div[1]/input')
    elem.send_keys(username)
    elem = driver.find_element_by_xpath('/html/body/div/div/div/div/form/div[2]/input')
    elem.send_keys(password + Keys.RETURN) #security won't be compromised because this is client-side only
except TimeoutException:
    print("Error 01")
    driver.quit()
time.sleep(2)


xpath_day = gotoDate(driver, init_year, init_month, init_day)
day = init_day
time.sleep(2)
date = date(init_year,init_month,init_day)
tDelta = timedelta(days=1)

for i in range(delta):
    
    try:
        elem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/div/div/portable-export/div/button[2]')))#driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/portable-export/div/button[2]')
        elem.click()
    except TimeoutException:
        print("Error 02")
 
    while not os.path.exists('/Users/macbookpro/Downloads/gm-dailyReport.csv'):
        time.sleep(1)
    moveData(date, fileName)
    date += tDelta
    
    if ((i+1)== delta):
        break
    nextDay(day,driver)
    day = day + 1
    time.sleep(1)






