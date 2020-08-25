from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    def __init__(self, driver_base = None):
        if driver_base is None:
            option = Options()
            option.debugger_address="localhost:9222"
            self.driver = webdriver.Chrome(options=option)
        else:
            self.driver:WebDriver = driver_base

        self.driver.implicitly_wait(3)

    def find(self, by, selector):
        return self.driver.find_element(by, selector)

    def finds(self, by, selector):
        return self.driver.find_elements(by, selector)