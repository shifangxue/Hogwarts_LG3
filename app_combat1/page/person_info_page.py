from appium.webdriver.common.mobileby import MobileBy

from app_combat1.page.base_page import BasePage
from app_combat1.page.edit_member_page import EditMemberPage


class PersonInfoPage(BasePage):
    def menu(self):
        self.find(MobileBy.ID, 'com.tencent.wework:id/hvd').click()
        self.find(MobileBy.ID, 'com.tencent.wework:id/b87').click()
        return EditMemberPage(self.driver)