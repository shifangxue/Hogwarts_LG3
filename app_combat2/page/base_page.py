from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:

    # 初使化，启动企业微信并登陆
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

    # 封装查找页面元素并返回
    def find(self, by: MobileBy, sn: str):
        return self.driver.find_element(by, sn)

    # 关闭app
    def close(self):
        self.driver.quit()

    # 查找元素并单击
    def find_and_click(self, by: MobileBy, sn: str):
        self.find(by, sn).click()

    # 查找元素并输入
    def find_and_sendKeys(self, by: MobileBy, sn: str, key: str) -> None:
        self.find(by, sn).send_keys(key)

    # 获取元素文本信息
    def find_and_getText(self, by: MobileBy, sn: str):
        return self.find(by, sn).text
