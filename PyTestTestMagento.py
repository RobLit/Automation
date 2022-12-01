import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_setup():
    global driver
    driver = webdriver.Edge(executable_path="F:/GitHub/testing/drivers/msedgedriver.exe")
    global list
    list = ["Basic", "Snug", "Base Layer", "Compression", "Capri", "Leggings", "Sweatpants", "Track Pants", "Parachute"]
    global list1
    list1 = ["Full Zip", "Sweatshirt", "Hoodie", "Pullover"]
    global list2
    list2 = ["Tank", "Tee", "Insulated", "Heavy Duty", "Soft Shell", "¼ zip", "Lightweight", "Hooded", "Hard Shell", "Windbreaker", "Full Zip", "Jacket", "Rain Coat"]


def test_one():
    driver.get("https://magento.softwaretestingboard.com/women/bottoms-women.html?product_list_limit=36")
    for n in range(1, 26):
        driver.find_element(By.XPATH, ('//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[%d]/div/a/span/span/img' %n)).click()
        driver.find_element(By.LINK_TEXT, "More Information").click()
        NAME = driver.find_element(By.XPATH, '//*[@data-th="Style"]').text.split(', ')
        ID = driver.find_element(By.CLASS_NAME, "value").text
        elements_in_list = [elem for elem in NAME if elem in list]
        for got_element in NAME:
            if not got_element in list:
                print(f"Retrieved element {got_element} not in list {list} at ", ID)
        driver.back()
    if not got_element in list:
        with pytest.raises(AssertionError):
            pytest.fail("Some elements are not in list")


def test_two():
    driver.get("https://magento.softwaretestingboard.com/women/tops-women/hoodies-and-sweatshirts-women.html")
    for n in range(1, 12):
        driver.find_element(By.XPATH, ('//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[%d]' %n)).click()
        driver.find_element(By.LINK_TEXT, "More Information").click()
        NAME = driver.find_element(By.XPATH, '//*[@data-th="Style"]').text.split(', ')
        ID = driver.find_element(By.CLASS_NAME, "value").text
        elements_in_list1 = [elem for elem in NAME if elem in list1]
        for got_element in NAME:
            if not got_element in list1:
                print(f"Retrieved element {got_element} not in list1 {list1} at ", ID)
        driver.back()
    if not got_element in list1:
        raise AssertionError ("Some elements are not in list")


def test_three():
    driver.get("https://magento.softwaretestingboard.com/men/tops-men.html?product_list_limit=36")
    for n in range(1, 36):
        driver.find_element(By.XPATH, ('//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[%d]' %n)).click()
        driver.find_element(By.LINK_TEXT, "More Information").click()
        NAME = driver.find_element(By.XPATH, '//*[@data-th="Style"]').text.split(', ')
        ID = driver.find_element(By.CLASS_NAME, "value").text
        elements_in_list1 = [elem for elem in NAME if elem in list1]
        for got_element in NAME:
            if not got_element in list2:
                print(f"Retrieved element {got_element} not in list2 {list1} at ", ID)
        driver.back()
    driver.find_element(By.CLASS_NAME, "page").click()
    for n in range(1, 12):
        driver.find_element(By.XPATH, ('//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[%d]' % n)).click()
        driver.find_element(By.LINK_TEXT, "More Information").click()
        NAME = driver.find_element(By.XPATH, '//*[@data-th="Style"]').text.split(', ')
        ID = driver.find_element(By.CLASS_NAME, "value").text
        elements_in_list2 = [elem for elem in NAME if elem in list2]
        for got_element in NAME:
            if not got_element in list2:
                print(f"Retrieved element {got_element} not in list2 {list2} at ", ID)
        driver.back()
    if not got_element in list2:
        raise AssertionError ("Some elements are not in list")


def test_teardown():
    driver.close()

#"Basic",
#PyTest napisać błąd w przypadku if not element in list
#PyTest napisać błąd w przypadku element is not clickable

