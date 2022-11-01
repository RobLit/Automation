from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
import string

import selenium

driver=webdriver.Edge(executable_path="F:/GitHub/testing/drivers/msedgedriver.exe")
#required downloaded webdriver and copied path to this file here /\

driver.maximize_window()
driver.get("http://www.fakemailgenerator.com/")
email = driver.find_element(By.ID, "cxtEmail").text
print(email)

actions = ActionChains(driver)
about = driver.find_element(By.LINK_TEXT, "FAQ")
actions.key_down(Keys.CONTROL).click(about).key_up(Keys.CONTROL).perform()

driver.switch_to.window(driver.window_handles[-1])
driver.get("https://www.fakenamegenerator.com/")
name = driver.find_element(By.XPATH, ('//*[@id="details"]/div[2]/div[2]/div/div[1]/h3')).text
print(name)
surname = driver.find_element(By.XPATH, ('//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[10]/dd')).text
print(surname)

characters = string.ascii_letters + string.digits
password = ''.join(random.choice(characters) for i in range(10))
print(password)

driver.switch_to.window(driver.window_handles[-1])
driver.get("https://automationintesting.com/selenium/testpage/")
driver.find_element(By.ID, "firstname").send_keys(name)
driver.find_element(By.ID, "surname").send_keys(surname)
driver.find_element(By.XPATH, ('//*[@id="gender"]/option[4]')).click()
driver.find_element(By.ID, "blue").click()
driver.find_element(By.XPATH, ('//*[@id="contactus"]/div[5]/div/label/textarea')).send_keys(password)
driver.find_element(By.XPATH, ('//*[@id="continent"]/option[6]')).click()
driver.find_element(By.ID, "checkbox1").click()


