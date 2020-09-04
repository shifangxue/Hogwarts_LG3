from appium.webdriver.common.mobileby import MobileBy

from app_combat1.page.base_page import BasePage
from app_combat1.page.contact_page import ContactPage


class MainPage(BasePage):

    def go_to_contact(self):
        # 点击通讯录，转向通讯录页面
        self.find(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return ContactPage(self.driver)
