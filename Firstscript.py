import time

from selenium import webdriver

driver=webdriver.Chrome("C:/Users/crochet/PycharmProjects/TestpythonProject/Chrome/chromedriver.exe")
driver.maximize_window()
driver.get("http://mylagrolara.1wayit.com")
time.sleep(5)
driver.find_element_by_xpath("//*[@id='navbarsExample09']/ul[2]/li[3]/a") .click()
time.sleep(10)

driver.close()
#element.click()
print("Executed")a
