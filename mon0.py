from selenium import webdriver
from selenium.webdriver.common.by import By
import sqlite3

import time

conn = sqlite3.connect('Stockdata.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS stockdata(price FLOAT, change FLOAT)') ###############Table Creation####################

driver = webdriver.Chrome()
driver.get("https://finance.yahoo.com")
#try :
markets = driver.find_element_by_xpath("//a[@title='Markets']")
markets.click()

#except:




time.sleep(10)

stockList = driver.find_element_by_link_text("Stocks: Most Actives")
stockList.click()

run = 0

current = ['', '', '']

time.sleep(15)
while run==0 :

    topStock = driver.find_element_by_xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr[2]/td[1]')
    stock1Name = topStock.text

    topStockPrice = driver.find_element_by_xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr[2]/td[3]')
    topStockPriceText = topStockPrice.text

    topStockChange = driver.find_element_by_xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr[2]/td[5]')
    topStockChangeText = topStockChange.text

    topStockProperties = [stock1Name, topStockPriceText, topStockChangeText]


    if current != topStockProperties:

        price = float(topStockPriceText)

        percentage = ''

        for i in range(len(topStockChangeText)-1):

            percentage = percentage + topStockChangeText[i]

        print(price)
        percentageFloat = float(percentage)
        print(percentageFloat)

        print(topStockProperties)

        c.execute('INSERT INTO stockdata (price, change) VALUES (?, ?)', (price, percentageFloat))
        conn.commit()

        current = topStockProperties

c.close()
conn.close()