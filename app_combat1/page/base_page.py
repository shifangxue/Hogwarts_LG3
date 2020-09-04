from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:

    def __init__(self, driver_base=None):
        if driver_base is None:
            caps = {"platformName": "android",
                    "deviceName": "device-1",
                    "appPackage": "com.tencent.wework",
                    "appActivity": ".launch.WwMainActivity",
                    "noReset": "True"}
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self.driver: WebDriver = driver_base

        self.driver.implicitly_wait(10)

    def find(self, by: MobileBy, sn: str):
        return self.driver.find_element(by, sn)

    def close(self):
        self.driver.quit()

