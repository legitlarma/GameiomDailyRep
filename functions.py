import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
import getpass
import os
from pathlib import Path

def getPath(name):
    pathName = str(os.path.join(Path.home(), name))
    return pathName

def monthToInt(month):
    if (month == 'Jan'):
        return 1
    if (month == 'Feb'):
        return 2
    if (month == 'Mar'):
        return 3
    if (month == 'Apr'):
        return 4
    if (month == 'May'):
        return 5
    if (month == 'Jun'):
        return 6
    if (month == 'Jul'):
        return 7
    if (month == 'Aug'):        
        return 8
    if (month == 'Sep'):
        return 9
    if (month == 'Oct'):
        return 10
    if (month == 'Nov'):
        return 11
    if (month == 'Dec'):
        return 12
def gotoDate(driver, year, month, day):
    elem = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/portable-day-filter/section/div/div/a')          #click date drop down
    elem.click()
    elem = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/portable-day-filter/section/div/div/ul/div/table/thead/tr[1]/th[2]')     #go back to year
    elem.click()
    time.sleep(1)
    elem.click()
    time.sleep(1)
    elem.click()
    
    while True:
        elem_first = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/portable-day-filter/section/div/div/ul/div/table/tbody/tr/td/span[1]')      #first year in list
        elem_last = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/portable-day-filter/section/div/div/ul/div/table/tbody/tr/td/span[12]')
        if (int(elem_first.text) > year): #does the tabel of years need to change? 
            elem = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/portable-day-filter/section/div/div/ul/div/table/thead/tr[1]/th[1]')
            elem.click()
        elif (int(elem_last.text) < year):
            elem = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/portable-day-filter/section/div/div/ul/div/table/thead/tr[1]/th[3]')
            elem.click()
        else:
            break
    i = 1
    while (i != 13):        #find correct year
        xpath_ele = '/html/body/div/div[2]/div/div/div/portable-day-filter/section/div/div/ul/div/table/tbody/tr/td/span['+str(i)+']'       #iterate through years
        newelem = driver.find_element_by_xpath(xpath_ele)
        #print(newelem.text)
        if (int(newelem.text) == year):
            newelem.click()
            break
        else:
            i = i + 1
            continue
    i = 1
    while (i != 13):        #find correct month
        xpath_ele = '/html/body/div/div[2]/div/div/div/portable-day-filter/section/div/div/ul/div/table/tbody/tr/td/span['+str(i)+']'       #iterate through years
        newelem = driver.find_element_by_xpath(xpath_ele)
        #print(newelem.text)
        if (monthToInt(newelem.text) == month):
            newelem.click()
            break
        else:
            i = i + 1
            continue

    done = False
    for i in range(6):
        for j in range(7):
            xpath_ele = '/html/body/div/div[2]/div/div/div/portable-day-filter/section/div/div/ul/div/table/tbody/tr['+str(i+1)+']/td['+str(j+1)+']'
            newelem = driver.find_element_by_xpath(xpath_ele)
            if (int(newelem.text) == day):
                newelem.click()
                done = True
                return xpath_ele
            else:
                continue

        if (done == True):
            break
        else:
            continue
            

    
def nextDay(prevDate, driver):   #go to next day
    done = False
    elem = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/portable-day-filter/section/div/div/a')          #click date drop down
    elem.click()
    for i in range(6):
        for j in range(7):
            xpath_ele = '/html/body/div/div[2]/div/div/div/portable-day-filter/section/div/div/ul/div/table/tbody/tr['+str(i+1)+']/td['+str(j+1)+']'
            newelem = driver.find_element_by_xpath(xpath_ele)
            if (int(newelem.text) == (prevDate+1)):
                text = newelem.text
                newelem.click()
                done = True
                return text
            else:
                continue

        if (done == True):
            break
        else:
            continue
        
    #return xpath for next day
