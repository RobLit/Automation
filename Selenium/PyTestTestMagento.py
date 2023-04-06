import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_setup():
    global driver
    driver = webdriver.Edge(executable_path="GitTest/drivers/msedgedriver.exe")
    global list
    list = ["Basic", "Snug", "Base Layer", "Compression", "Capri", "Leggings", "Sweatpants", "Track Pants", "Parachute"]
    global list1
    list1 = ["Full Zip", "Sweatshirt", "Hoodie", "Pullover"]
    global list2
    list2 = ["Tank", "Tee", "Insulated", "Heavy Duty", "Soft Shell", "¼ zip", "Lightweight", "Hooded", "Hard Shell",
             "Windbreaker", "Full Zip", "Jacket", "Rain Coat"]
    global list3
    list3 = ["Base Layer", "Compression", "Tights", "Workout Pants", "Leggings", "Track Pants", "Sweatpants"]

def test_one_BottomsWomen():
    driver.get("https://magento.softwaretestingboard.com/women/bottoms-women.html?product_list_limit=36")
    for n in range(1, 26):
        try:
            driver.find_element(By.XPATH, ('//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[%d]/div/a/span/span/img' % n)).click()
        except:
            AssertionError()
        try:
            driver.find_element(By.LINK_TEXT, "More Information").click()
        except:
            AssertionError()
        try:
            NAME = driver.find_element(By.XPATH, '//*[@data-th="Style"]').text.split(', ')
        except:
            AssertionError()
        try:
            ID = driver.find_element(By.CLASS_NAME, "value").text
        except:
            AssertionError()
        elements_in_list = [elem for elem in NAME if elem in list]
        for got_element in NAME:
            if not got_element in list:
                raise AssertionError(f"Retrieved element {got_element} not in list {list} at ", ID)
        driver.back()

def test_two_TopsWomen():
    driver.get("https://magento.softwaretestingboard.com/women/tops-women/hoodies-and-sweatshirts-women.html")
    for n in range(1, 12):
        try:
            driver.find_element(By.XPATH, ('//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[%d]' % n)).click()
        except:
            AssertionError()
        try:
            driver.find_element(By.LINK_TEXT, "More Information").click()
        except:
            AssertionError()
        try:
            NAME = driver.find_element(By.XPATH, '//*[@data-th="Style"]').text.split(', ')
        except:
            AssertionError()
        try:
            ID = driver.find_element(By.CLASS_NAME, "value").text
        except:
            AssertionError()
        elements_in_list1 = [elem for elem in NAME if elem in list1]
        for got_element in NAME:
            if not got_element in list1:
                raise AssertionError(f"Retrieved element {got_element} not in list1 {list1} at ", ID)
        driver.back()

def test_three_TopsMen():
    driver.get("https://magento.softwaretestingboard.com/men/tops-men.html?product_list_limit=36")
    for n in range(1, 36):
        try:
            driver.find_element(By.XPATH, ('//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[%d]' % n)).click()
        except:
            AssertionError()
        try:
            driver.find_element(By.LINK_TEXT, "More Information").click()
        except:
            AssertionError()
        try:
            NAME = driver.find_element(By.XPATH, '//*[@data-th="Style"]').text.split(', ')
        except:
            AssertionError
        try:
            ID = driver.find_element(By.CLASS_NAME, "value").text
        except:
            AssertionError
        elements_in_list1 = [elem for elem in NAME if elem in list1]
        for got_element in NAME:
            if not got_element in list2:
                raise AssertionError(f"Retrieved element {got_element} not in list {list2} at ", ID)
        driver.back()

    driver.find_element(By.CLASS_NAME, "page").click()
    for n in range(1, 12):
        try:
            driver.find_element(By.XPATH, ('//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[%d]' % n)).click()
        except:
            AssertionError()
        try:
            driver.find_element(By.LINK_TEXT, "More Information").click()
        except:
            AssertionError()
        try:
            NAME = driver.find_element(By.XPATH, '//*[@data-th="Style"]').text.split(', ')
        except:
            AssertionError()
        try:
            ID = driver.find_element(By.CLASS_NAME, "value").text
        except:
            AssertionError()
        elements_in_list2 = [elem for elem in NAME if elem in list2]
        for got_element in NAME:
            if not got_element in list2:
                raise AssertionError(f"Retrieved element {got_element} not in list {list2} at ", ID)
        driver.back()

def test_four_BottomsMen():
    driver.get("https://magento.softwaretestingboard.com/men/bottoms-men.html?product_list_limit=36")
    for n in range(1, 24):
        try:
            driver.find_element(By.XPATH, ('//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[%d]/div/a/span/span/img' % n)).click()
        except:
            AssertionError()
        try:
            driver.find_element(By.LINK_TEXT, "More Information").click()
        except:
            AssertionError()
        try:
            NAME = driver.find_element(By.XPATH, '//*[@data-th="Style"]').text.split(', ')
        except:
            AssertionError()
        try:
            ID = driver.find_element(By.CLASS_NAME, "value").text
        except:
            AssertionError()
        elements_in_list = [elem for elem in NAME if elem in list3]
        for got_element in NAME:
            if not got_element in list3:
                raise AssertionError(f"Retrieved element {got_element} not in list {list3} at ", ID)
        driver.back()
def test_teardown():
    driver.close()

