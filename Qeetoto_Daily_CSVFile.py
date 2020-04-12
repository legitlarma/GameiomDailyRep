import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
username = input("Enter Gameiom username: ")
password = getpass.getpass("Password: ") #privately gets password (only in terminal, doesn't work on IDEs)

driver = webdriver.Chrome('/Users/macbookpro/Desktop/chromedriver')
driver.get('https://cdn.gameiom.com/gameiom/backoffice/production/latest/index.html#dailyReport');

try:
    elem = driver.find_element_by_id('form-signin-email')
    elem.send_keys(username)
finally:
    print("Error 00")
    driver.quit()
try:
    elem = driver.find_element_by_xpath('/html/body/div/div/div/div/form/div[2]/input')
    elem.send_keys(password + Keys.RETURN)
finally:
    print("Error 01")
    driver.quit()
try:
    elem = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/portable-export/div/button[2]')
    elem.click()
finally:
    print("Error 02")
    driver.quit()







