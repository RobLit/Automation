from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WaitExcTypes
import re

def test_setup():
    global driver
    driver = webdriver.Edge(executable_path="GitTest/drivers/msedgedriver.exe")

def test_oneZalandoSales():

    driver.get("https://www.zalando.pl/okazje/?sale=true")
    print("Test started")
    for n in range(2, 500):
        for i in range(1, 100):
            try:
                NAME = driver.find_element(By.XPATH, ('//*[@id="main-content"]/div/div/div[7]/div/div[2]/div[2]/div[2]/div[%d]/div/article/div[4]/a/header/div[1]/h3[2]' %i)).text
            except:
                continue
            try:
                BEFORE = driver.find_element(By.XPATH, ('//*[@id="main-content"]/div/div/div[7]/div/div[2]/div[2]/div[2]/div[%d]/div/article/div[4]/a/header/div[2]/span/p[2]' %i)).text
            except:
                continue
            try:
                AFTER = driver.find_element(By.XPATH, ('//*[@id="main-content"]/div/div/div[7]/div/div[2]/div[2]/div[2]/div[%d]/div/article/div[4]/a/header/div[2]/p' %i)).text
            except:
                continue
            try:
                SALEPERCENT = driver.find_element(By.XPATH, ('//*[@id="main-content"]/div/div/div[7]/div/div[2]/div[2]/div[2]/div[%d]/div/article/div[4]/a/header/div[2]/span/p[3]' %i)).text
            except:
                continue
            BEFORE2 = BEFORE.removesuffix("zł").replace(",", ".").replace(" ","")
            AFTER2 = AFTER.removeprefix("od").removesuffix("zł").replace(",", ".").replace(" ","")
            SALEPERCENT2 = SALEPERCENT.removeprefix("nawet").replace("-","").removesuffix("%")
            PERCENT =  round(100-(float(AFTER2)/float(BEFORE2)*100))
            if PERCENT != SALEPERCENT2:
                AssertionError("There is problem with"+NAME)
            else:
                print("Testing done")
        try:
            driver.get("https://www.zalando.pl/okazje/?sale=true&p=%d" %n)
        except:
            driver.close()