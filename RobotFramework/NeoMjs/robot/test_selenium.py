from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge(executable_path="E:/usr/local/bin/msedgedriver.exe")

driver.get("http://localhost:8080/dist/production/apps/realworld/index.html")
sleep(5)
text = driver.find_element(By.ID, "neo-vnode-33").text
print(text)
driver.find_element(By.ID, "neo-vnode-35").click()
text2 = driver.find_element(By.CLASS_NAME, "counter").text
print(text2)