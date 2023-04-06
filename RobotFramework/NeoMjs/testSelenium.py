from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge(executable_path="E:/us/local/bin/msedgedriver.exe")

#driver.get("http://www.google.com")
#driver.find_element(By.ID, "L2AGLb").click()

driver.get("http://localhost:8080/dist/development/apps/realworld/index.html/")
text = driver.find_element(By.ID, "neo-vnode-35").text
print(text)
