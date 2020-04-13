import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
from functions import *
username = input("Enter Gameiom username: ")
password = getpass.getpass("Password: ") #privately gets password (only in terminal, doesn't work on IDEs)

driver = webdriver.Chrome('/Users/macbookpro/Desktop/chromedriver')
driver.get('https://cdn.gameiom.com/gameiom/backoffice/production/latest/index.html#dailyReport');
delay = 3
GameiomLogin(username, password, driver, delay)






try:
    elem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/div/div/portable-export/div/button[2]')))
    elem.click()
except TimeoutException:
    print("Error 02")
    driver.quit()







