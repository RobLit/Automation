from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WaitExcTypes

def test_setupZalandoSales():

    global driver
    driver = webdriver.Edge(executable_path="GitTest/drivers/msedgedriver.exe")


def test_oneZalandoCheckout():

    driver.get("https://www.zalando.pl/okazje/?sale=true")

    for n in range(2, 5):
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
            print(NAME, BEFORE, AFTER, SALEPERCENT)
        driver.get("https://www.zalando.pl/okazje/?sale=true&p=%d" %n)


        BEFORE2 = []
        AFTER2 = []




        #PRICE = 100 - (AFTER2 / BEFORE2)
        #print(PRICE)

#re.sub(' zł', '', float)
#428