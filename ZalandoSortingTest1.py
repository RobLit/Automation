from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
import pytest


def test_setup():
    global driver
    driver = webdriver.Edge(executable_path="GitTest/drivers/msedgedriver.exe")

def test_oneZalandoASC():
    driver.get("https://www.zalando.pl/dzieci-akcesoria/?order=price&dir=asc")
    for n in range (2, 65):
        for i in range (1, 100):
            try:
                NAME = driver.find_element(By.XPATH, ('//*[@id="main-content"]/div/div/div[7]/div/div[2]/div[2]/div[2]/div[%d]' %i)).text
                PRICE = driver.find_element(By.XPATH, ('//*[@id="main-content"]/div/div/div[7]/div/div[2]/div[2]/div[2]/div[%d]/div/article/div[4]/a/header/section/p' %i)).text
                PRICE2 = driver.find_element(By.XPATH, ('//*[@id="main-content"]/div/div/div[7]/div/div[2]/div[2]/div[2]/div[%d+1]/div/article/div[4]/a/header/section/p' %i)).text
                PRICE3 = float(PRICE.removeprefix("od").replace(" ", "").replace(",", ".").removesuffix("zł"))
                PRICE4 = float(PRICE2.removeprefix("od").replace(" ", "").replace(",", ".").removesuffix("zł"))
                if PRICE4 < PRICE3:
                    pytest.fail("There is problem with:" + " " + NAME)
            except NoSuchElementException:
                continue
        driver.get("https://www.zalando.pl/dzieci-akcesoria/?p=%d&order=price&dir=asc" %n)
    print("Testing done")

def test_twoZalandoDESC():
    driver.get("https://www.zalando.pl/dzieci-akcesoria/?order=price&dir=desc")
    for n in range(2, 65):
        for i in range(1, 100):
            try:
                NAME = driver.find_element(By.XPATH, ('//*[@id="main-content"]/div/div/div[7]/div/div[2]/div[2]/div[2]/div[%d]' % i)).text
                PRICE = driver.find_element(By.XPATH, ('//*[@id="main-content"]/div/div/div[7]/div/div[2]/div[2]/div[2]/div[%d]/div/article/div[4]/a/header/section/p' % i)).text
                PRICE2 = driver.find_element(By.XPATH, ('//*[@id="main-content"]/div/div/div[7]/div/div[2]/div[2]/div[2]/div[%d+1]/div/article/div[4]/a/header/section/p' % i)).text
                PRICE3 = float(PRICE.removeprefix("od").replace(" ", "").replace(",", ".").removesuffix("zł"))
                PRICE4 = float(PRICE2.removeprefix("od").replace(" ", "").replace(",", ".").removesuffix("zł"))
                if PRICE4 > PRICE3:
                    pytest.fail("There is problem with:" + " " + NAME)
            except NoSuchElementException:
                continue
        driver.get("https://www.zalando.pl/dzieci-akcesoria/?p=%d&order=price&dir=desc" % n)
    print("Testing done")
