import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge(executable_path="GitTest/drivers/msedgedriver.exe")

global PSWD
PSWD = "secret_sauce"
global FNM
FNM = "Test"
global LNM
LNM = "Test"
global ZIP
ZIP = "911"
global ITEM
ITEM = [4, 0, 1, 5, 2, 3]
global NAME
NAME = ["add-to-cart-sauce-labs-backpack", "add-to-cart-sauce-labs-bike-light", "add-to-cart-sauce-labs-bolt-t-shirt", "add-to-cart-sauce-labs-fleece-jacket", "add-to-cart-sauce-labs-onesie", "add-to-cart-test.allthethings()-t-shirt-(red)"]
global RMV
RMV = ["remove-sauce-labs-backpack", "remove-sauce-labs-bike-light", "remove-sauce-labs-bolt-t-shirt", "remove-sauce-labs-fleece-jacket", "remove-sauce-labs-onesie", "remove-test.allthethings()-t-shirt-(red)"]

def test_sauce_1():
    for lst2, lst3, lst4 in zip(ITEM, NAME, RMV):
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys(PSWD)
        driver.find_element(By.ID, "login-button").click()
        URL = "https://www.saucedemo.com/inventory.html"
        assert URL == driver.current_url
        if URL != driver.current_url:
            return pytest.fail("There is problem with login on 'standard_user'")
        try:
            NAME2 = driver.find_element(By.ID, "item_%d_title_link" % lst2).text
        except:
            pytest.fail("Element can't be found!")
        try:
            driver.find_element(By.XPATH, (f'//*[@id="{lst3}"]')).click()
        except:
            pytest.fail("Element adding to cart can't be found!")
        try:
            driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        except:
            pytest.fail("Shopping cart link can't be found!")
        CART = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        if NAME2 != CART:
            pytest.fail("Cart didn't match with" + " " + NAME2)
        try:
            driver.find_element(By.ID, "checkout").click()
            driver.find_element(By.ID, "first-name").send_keys(FNM)
            driver.find_element(By.ID, "last-name").send_keys(LNM)
            driver.find_element(By.ID, "postal-code").send_keys(ZIP)
            driver.find_element(By.ID, "continue").click()
        except:
            pytest.fail("There is problem with filling data in checkout")
        PRICE = driver.find_element(By.XPATH, ('//*[@id="checkout_summary_container"]/div/div[2]/div[5]')).text
        TAX = driver.find_element(By.XPATH, ('//*[@id="checkout_summary_container"]/div/div[2]/div[6]')).text
        TOTAL = driver.find_element(By.XPATH, ('//*[@id="checkout_summary_container"]/div/div[2]/div[7]')).text
        PRC = float(PRICE.removeprefix("Item total:").replace("$", ""))
        TX = float(TAX.removeprefix("Tax:").replace("$", ""))
        TTL = float(TOTAL.removeprefix("Total:").replace("$", ""))
        TTL1 = PRC + TX
        rTTL = round(TTL, 2)
        rTTL1 = round(TTL1, 2)
        if rTTL1 != rTTL:
            pytest.fail("There is problem with price in " + " " + NAME2 + "and standard_user")
        driver.find_element(By.ID, "finish").click()
        driver.find_element(By.NAME, "back-to-products").click()
        try:
            EC.element_to_be_clickable(driver.find_element(By.XPATH, (f'//*[@id="{lst4}"]')).click())
            print("Shopping cart wasn't empty!")
        except:
            continue

#@pytest.mark.parametrize('lst3', ["add-to-cart-sauce-labs-backpack", "add-to-cart-sauce-labs-bike-light", "add-to-cart-sauce-labs-bolt-t-shirt", "add-to-cart-sauce-labs-fleece-jacket", "add-to-cart-sauce-labs-onesie", "add-to-cart-test.allthethings()-t-shirt-(red)"], ids=str)
def test_sauce_2():
    for lst2, lst3, lst4 in zip(ITEM, NAME, RMV):
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        driver.find_element(By.ID, "password").send_keys(PSWD)
        driver.find_element(By.ID, "login-button").click()
        URL = "https://www.saucedemo.com/inventory.html"
        assert URL == driver.current_url
        if URL != driver.current_url:
            return pytest.fail("There is problem with login on locked_out_user")
        try:
            NAME2 = driver.find_element(By.ID, "item_%d_title_link" % lst2).text
        except:
            pytest.fail("Element can't be found!")
        try:
            driver.find_element(By.XPATH, (f'//*[@id="{lst3}"]')).click()
        except:
            pytest.fail("Element adding to cart can't be found!")
        try:
            driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        except:
            pytest.fail("Shopping cart link can't be found!")
        CART = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        if NAME2 != CART:
            pytest.fail("Cart didn't match with" + " " + NAME2)
        try:
            driver.find_element(By.ID, "checkout").click()
            driver.find_element(By.ID, "first-name").send_keys(FNM)
            driver.find_element(By.ID, "last-name").send_keys(LNM)
            driver.find_element(By.ID, "postal-code").send_keys(ZIP)
            driver.find_element(By.ID, "continue").click()
        except:
            pytest.fail("There is problem with filling data in checkout")
        PRICE = driver.find_element(By.XPATH, ('//*[@id="checkout_summary_container"]/div/div[2]/div[5]')).text
        TAX = driver.find_element(By.XPATH, ('//*[@id="checkout_summary_container"]/div/div[2]/div[6]')).text
        TOTAL = driver.find_element(By.XPATH, ('//*[@id="checkout_summary_container"]/div/div[2]/div[7]')).text
        PRC = float(PRICE.removeprefix("Item total:").replace("$", ""))
        TX = float(TAX.removeprefix("Tax:").replace("$", ""))
        TTL = float(TOTAL.removeprefix("Total:").replace("$", ""))
        TTL1 = PRC + TX
        rTTL = round(TTL, 2)
        rTTL1 = round(TTL1, 2)
        if rTTL1 != rTTL:
            pytest.fail("There is problem with price in " + " " + NAME2 + "and standard_user")
        driver.find_element(By.ID, "finish").click()
        driver.find_element(By.NAME, "back-to-products").click()
        try:
            EC.element_to_be_clickable(driver.find_element(By.XPATH, (f'//*[@id="{lst4}"]')).click())
            print("Shopping cart wasn't empty!")
        except:
            continue

def test_sauce_3():
    for lst2, lst3, lst4 in zip(ITEM, NAME, RMV):
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("problem_user")
        driver.find_element(By.ID, "password").send_keys(PSWD)
        driver.find_element(By.ID, "login-button").click()
        URL = "https://www.saucedemo.com/inventory.html"
        assert URL == driver.current_url
        if URL != driver.current_url:
            return pytest.fail("There is problem with login on problem_user")
        try:
            NAME2 = driver.find_element(By.ID, "item_%d_title_link" % lst2).text
        except:
            pytest.fail("Element can't be found!")
        try:
            driver.find_element(By.XPATH, (f'//*[@id="{lst3}"]')).click()
        except:
            pytest.fail("Element adding to cart can't be found!")
        try:
            driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        except:
            pytest.fail("Shopping cart link can't be found!")
        CART = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        if NAME2 != CART:
            pytest.fail("Cart didn't match with" + " " + NAME2)
        try:
            driver.find_element(By.ID, "checkout").click()
            driver.find_element(By.ID, "first-name").send_keys(FNM)
            driver.find_element(By.ID, "last-name").send_keys(LNM)
            driver.find_element(By.ID, "postal-code").send_keys(ZIP)
            driver.find_element(By.ID, "continue").click()
        except:
            pytest.fail("There is problem with filling data in checkout")
        PRICE = driver.find_element(By.XPATH, ('//*[@id="checkout_summary_container"]/div/div[2]/div[5]')).text
        TAX = driver.find_element(By.XPATH, ('//*[@id="checkout_summary_container"]/div/div[2]/div[6]')).text
        TOTAL = driver.find_element(By.XPATH, ('//*[@id="checkout_summary_container"]/div/div[2]/div[7]')).text
        PRC = float(PRICE.removeprefix("Item total:").replace("$", ""))
        TX = float(TAX.removeprefix("Tax:").replace("$", ""))
        TTL = float(TOTAL.removeprefix("Total:").replace("$", ""))
        TTL1 = PRC + TX
        rTTL = round(TTL, 2)
        rTTL1 = round(TTL1, 2)
        if rTTL1 != rTTL:
            pytest.fail("There is problem with price in " + " " + NAME2 + "and standard_user")
        driver.find_element(By.ID, "finish").click()
        driver.find_element(By.NAME, "back-to-products").click()
        try:
            EC.element_to_be_clickable(driver.find_element(By.XPATH, (f'//*[@id="{lst4}"]')).click())
            print("Shopping cart wasn't empty!")
        except:
            continue

def test_sauce_4():
    for lst2, lst3, lst4 in zip(ITEM, NAME, RMV):
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("performance_glitch_user")
        driver.find_element(By.ID, "password").send_keys(PSWD)
        driver.find_element(By.ID, "login-button").click()
        URL = "https://www.saucedemo.com/inventory.html"
        assert URL == driver.current_url
        if URL != driver.current_url:
            return pytest.fail("There is problem with login on performance_glitch_user")
        try:
            NAME2 = driver.find_element(By.ID, "item_%d_title_link" % lst2).text
        except:
            pytest.fail("Element can't be found!")
        try:
            driver.find_element(By.XPATH, (f'//*[@id="{lst3}"]')).click()
        except:
            pytest.fail("Element adding to cart can't be found!")
        try:
            driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        except:
            pytest.fail("Shopping cart link can't be found!")
        CART = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        if NAME2 != CART:
            pytest.fail("Cart didn't match with" + " " + NAME2)
        try:
            driver.find_element(By.ID, "checkout").click()
            driver.find_element(By.ID, "first-name").send_keys(FNM)
            driver.find_element(By.ID, "last-name").send_keys(LNM)
            driver.find_element(By.ID, "postal-code").send_keys(ZIP)
            driver.find_element(By.ID, "continue").click()
        except:
            pytest.fail("There is problem with filling data in checkout")
        PRICE = driver.find_element(By.XPATH, ('//*[@id="checkout_summary_container"]/div/div[2]/div[5]')).text
        TAX = driver.find_element(By.XPATH, ('//*[@id="checkout_summary_container"]/div/div[2]/div[6]')).text
        TOTAL = driver.find_element(By.XPATH, ('//*[@id="checkout_summary_container"]/div/div[2]/div[7]')).text
        PRC = float(PRICE.removeprefix("Item total:").replace("$", ""))
        TX = float(TAX.removeprefix("Tax:").replace("$", ""))
        TTL = float(TOTAL.removeprefix("Total:").replace("$", ""))
        TTL1 = PRC + TX
        rTTL = round(TTL, 2)
        rTTL1 = round(TTL1, 2)
        if rTTL1 != rTTL:
            pytest.fail("There is problem with price in " + " " + NAME2 + "and standard_user")
        driver.find_element(By.ID, "finish").click()
        driver.find_element(By.NAME, "back-to-products").click()
        try:
            EC.element_to_be_clickable(driver.find_element(By.XPATH, (f'//*[@id="{lst4}"]')).click())
            print("Shopping cart wasn't empty!")
        except:
            continue
