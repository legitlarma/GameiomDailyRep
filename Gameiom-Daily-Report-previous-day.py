import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
from datetime import date, timedelta
from functions import *
from GetData import *
import os

delta = timedelta(days = 1)
downloadsPath = getPath('Downloads')
downloadsPath_W_CSV = str(downloadsPath + '/gm-dailyReport.csv')

username = input("Enter Gameiom username: ")
password = getpass.getpass("Password: ") #privately gets password (only in terminal, doesn't work on IDEs)

cDriverpath = str(os.path.dirname(os.path.abspath(__file__)))+ '/chromedriver'

driver = webdriver.Chrome(cDriverpath)
driver.get('https://cdn.gameiom.com/gameiom/backoffice/production/latest/index.html#dailyReport');
delay = 3
GameiomLogin(username, password, driver, delay)
time.sleep(2)

prevDay(date.today().day, driver)

time.sleep(2)
dest_filename = 'data.xlsx'
if not os.path.isfile(dest_filename):
    wb = Workbook()
    ws = wb.active
    wb.save(filename = dest_filename)
    


try:
    elem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/div/div/portable-export/div/button[2]')))
    elem.click()
except TimeoutException:
    print("Error 02")
    driver.quit()

moveData((date.today() - delta), 'data.xlsx', downloadsPath_W_CSV)


driver.quit()
