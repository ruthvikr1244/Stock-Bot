from selenium import webdriver
from selenium.webdriver.common.by import By
import sqlite3

import time

conn = sqlite3.connect('Stockdata.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS row1(name STRING, price FLOAT, change FLOAT)') ###############Table Creation####################
c.execute('CREATE TABLE IF NOT EXISTS row2(name STRING, price FLOAT, change FLOAT)') ###############Table Creation####################
c.execute('CREATE TABLE IF NOT EXISTS row3(name STRING, price FLOAT, change FLOAT)') ###############Table Creation####################
c.execute('CREATE TABLE IF NOT EXISTS row4(name STRING, price FLOAT, change FLOAT)') ###############Table Creation####################
c.execute('CREATE TABLE IF NOT EXISTS row5(name STRING, price FLOAT, change FLOAT)') ###############Table Creation####################


driver = webdriver.Chrome()
driver.get("https://finance.yahoo.com")
#try :
markets = driver.find_element_by_xpath("//a[@title='Markets']")
markets.click()

#except:




time.sleep(10)

stockList = driver.find_element_by_link_text("Stocks: Gainers")
stockList.click()

run = 0

current = ['', '', '']
current2 = ['', '', '']
current3 = ['', '', '']
current4 = ['', '', '']
current5 = ['', '', '']


time.sleep(15)
while run==0 :

    topStock = driver.find_element_by_xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr[1]/td[1]')
    stock1Name = topStock.text

    topStockPrice = driver.find_element_by_xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr[1]/td[3]')
    topStockPriceText = topStockPrice.text

    topStockChange = driver.find_element_by_xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr[1]/td[5]')
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

        c.execute('INSERT INTO row1 (name, price, change) VALUES (?, ?, ?)', (stock1Name, price, percentageFloat))
        conn.commit()

        current = topStockProperties

    topStock2 = driver.find_element_by_xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr[2]/td[1]')
    stock1Name2 = topStock2.text

    topStockPrice2 = driver.find_element_by_xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr[2]/td[3]')
    topStockPriceText2 = topStockPrice2.text

    topStockChange2 = driver.find_element_by_xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr[2]/td[5]')
    topStockChangeText2 = topStockChange2.text

    topStockProperties2 = [stock1Name2, topStockPriceText2, topStockChangeText2]

    if current2 != topStockProperties2:

        price2 = float(topStockPriceText2)

        percentage2 = ''

        for i in range(len(topStockChangeText2) - 1):
            percentage2 = percentage2 + topStockChangeText2[i]

        print(price2)
        percentageFloat2 = float(percentage2)
        print(percentageFloat2)

        print(topStockProperties2)

        c.execute('INSERT INTO row2 (name, price, change) VALUES (?, ?, ?)', (stock1Name2, price2, percentageFloat2))
        conn.commit()

        current2 = topStockProperties2

    topStock3 = driver.find_element_by_xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr[3]/td[1]')
    stock1Name3 = topStock3.text

    topStockPrice3 = driver.find_element_by_xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr[3]/td[3]')
    topStockPriceText3 = topStockPrice3.text

    topStockChange3 = driver.find_element_by_xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr[3]/td[5]')
    topStockChangeText3 = topStockChange3.text

    topStockProperties3 = [stock1Name3, topStockPriceText3, topStockChangeText3]

    if current3 != topStockProperties3:

        price3 = float(topStockPriceText3)

        percentage3 = ''

        for i in range(len(topStockChangeText3) - 1):
            percentage3 = percentage3 + topStockChangeText3[i]

        print(price3)
        percentageFloat3 = float(percentage3)
        print(percentageFloat3)

        print(topStockProperties3)

        c.execute('INSERT INTO row3 (name, price, change) VALUES (?, ?, ?)', (stock1Name3, price3, percentageFloat3))
        conn.commit()

        current3 = topStockProperties3

    topStock4 = driver.find_element_by_xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr[4]/td[1]')
    stock1Name4 = topStock4.text

    topStockPrice4 = driver.find_element_by_xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr[4]/td[3]')
    topStockPriceText4 = topStockPrice4.text

    topStockChange4 = driver.find_element_by_xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr[4]/td[5]')
    topStockChangeText4 = topStockChange4.text

    topStockProperties4 = [stock1Name4, topStockPriceText4, topStockChangeText4]

    if current4 != topStockProperties4:

        price4 = float(topStockPriceText4)

        percentage4 = ''

        for i in range(len(topStockChangeText4) - 1):
            percentage4 = percentage4 + topStockChangeText4[i]

        print(price4)
        percentageFloat4 = float(percentage4)
        print(percentageFloat4)

        print(topStockProperties4)

        c.execute('INSERT INTO row4 (name, price, change) VALUES (?, ?, ?)', (stock1Name4, price4, percentageFloat4))
        conn.commit()

        current4 = topStockProperties4

    topStock5 = driver.find_element_by_xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr[5]/td[1]')
    stock1Name5 = topStock5.text

    topStockPrice5 = driver.find_element_by_xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr[5]/td[3]')
    topStockPriceText5 = topStockPrice5.text

    topStockChange5 = driver.find_element_by_xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr[5]/td[5]')
    topStockChangeText5 = topStockChange5.text

    topStockProperties5 = [stock1Name5, topStockPriceText5, topStockChangeText5]

    if current5 != topStockProperties5:

        price5 = float(topStockPriceText5)

        percentage5 = ''

        for i in range(len(topStockChangeText5) - 1):
            percentage5 = percentage5 + topStockChangeText5[i]

        print(price5)
        percentageFloat5 = float(percentage5)
        print(percentageFloat5)

        print(topStockProperties5)

        c.execute('INSERT INTO row5 (name, price, change) VALUES (?, ?, ?)', (stock1Name5, price5, percentageFloat5))
        conn.commit()

        current5 = topStockProperties5

c.close()
conn.close()



