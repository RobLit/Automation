from selenium import webdriver
from selenium.webdriver.common.by import By

def test_setup():
    global driver
    driver = webdriver.Edge(executable_path="GitTest/drivers/msedgedriver.exe")

def test_ZalandoSortingPriceLow2High():
    driver.get("https://www.zalando.pl/dzieci-akcesoria/?order=price&dir=asc")
    for a in range(2, 67):
        for i in range(1, 100):
            try:
                NAME = driver.find_element(By.XPATH, ('//*[@id="main-content"]/div/div/div[7]/div/div[2]/div[2]/div[2]/div[%d]' % i)).text
                PRICE = driver.find_element(By.XPATH, ('//*[@id="main-content"]/div/div/div[7]/div/div[2]/div[2]/div[2]/div[%d]/div/article/div[5]/a/header/section/p' % i)).text
                PRICE3 = PRICE.removeprefix("od").replace(" ", "").removesuffix("zł")
                PRICE2 = driver.find_element(By.XPATH, ('//*[@id="main-content"]/div/div/div[7]/div/div[2]/div[2]/div[2]/div[%d+1]/div/article/div[5]/a/header/section/p' % i)).text
                PRICE4 = PRICE2.removeprefix("od").replace(" ", "").removesuffix("zł")
            except:
                NAME = driver.find_element(By.XPATH, ('//*[@id="main-content"]/div/div/div[7]/div/div[2]/div[2]/div[2]/div[%d]' % i)).text
                PRICE = driver.find_element(By.XPATH, ('//*[@id="main-content"]/div/div/div[7]/div/div[2]/div[2]/div[2]/div[%d]/div/article/div[4]/a/header/section/p' % i)).text
                PRICE3 = PRICE.removeprefix("od").replace(" ", "").removesuffix("zł")
                PRICE2 = driver.find_element(By.XPATH, ('//*[@id="main-content"]/div/div/div[7]/div/div[2]/div[2]/div[2]/div[%d+1]/div/article/div[4]/a/header/section/p' % i)).text
                PRICE4 = PRICE2.removeprefix("od").replace(" ", "").removesuffix("zł")
            finally:
                if PRICE3 > PRICE4:
                    print("There is problem with:" + NAME)
                continue
        driver.get("https://www.zalando.pl/dzieci-akcesoria/?p=%d&order=price&dir=desc" % a)
    print("Test done")

def test_ZalandoSortingPriceHigh2Low():
    driver.get("https://www.zalando.pl/dzieci-akcesoria/?order=price&dir=desc")
    for a in range(2, 67):
        for i in range(1, 100):
            try:
                NAME = driver.find_element(By.XPATH, ('//*[@id="main-content"]/div/div/div[7]/div/div[2]/div[2]/div[2]/div[%d]' % i)).text
                PRICE = driver.find_element(By.XPATH, ('//*[@id="main-content"]/div/div/div[7]/div/div[2]/div[2]/div[2]/div[%d]/div/article/div[5]/a/header/section/p' % i)).text
                PRICE3 = PRICE.removeprefix("od").replace(" ", "").removesuffix("zł")
                PRICE2 = driver.find_element(By.XPATH, ('//*[@id="main-content"]/div/div/div[7]/div/div[2]/div[2]/div[2]/div[%d+1]/div/article/div[5]/a/header/section/p' % i)).text
                PRICE4 = PRICE2.removeprefix("od").replace(" ", "").removesuffix("zł")
            except:
                NAME = driver.find_element(By.XPATH, ('//*[@id="main-content"]/div/div/div[7]/div/div[2]/div[2]/div[2]/div[%d]' % i)).text
                PRICE = driver.find_element(By.XPATH, ('//*[@id="main-content"]/div/div/div[7]/div/div[2]/div[2]/div[2]/div[%d]/div/article/div[4]/a/header/section/p' % i)).text
                PRICE3 = PRICE.removeprefix("od").replace(" ", "").removesuffix("zł")
                PRICE2 = driver.find_element(By.XPATH, ('//*[@id="main-content"]/div/div/div[7]/div/div[2]/div[2]/div[2]/div[%d+1]/div/article/div[4]/a/header/section/p' % i)).text
                PRICE4 = PRICE2.removeprefix("od").replace(" ", "").removesuffix("zł")
            finally:
                if PRICE3 < PRICE4:
                    print("There is problem with:" + NAME)
                continue
        driver.get("https://www.zalando.pl/dzieci-akcesoria/?p=%d&order=price&dir=desc" % a)
    print("Test done")

