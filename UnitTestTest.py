import unittest
import self as self
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestSelenium1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge(executable_path="F:/GitHub/testing/drivers/msedgedriver.exe")

    def test_one(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://a.testaddressbook.com/")

        WebDriverWait(driver, 5).until(EC.title_contains("Sign In"))

    def tearDown(self):
        self.driver.close()
    if __name__ == "__main__":
        unittest.main()

class TestSelenium2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge(executable_path="F:/GitHub/testing/drivers/msedgedriver.exe")

    def test_two(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://a.testaddressbook.com/")




    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()