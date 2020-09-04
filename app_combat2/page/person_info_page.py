from appium.webdriver.common.mobileby import MobileBy

from app_combat2.page.base_page import BasePage
from app_combat2.page.edit_member_page import EditMemberPage


class PersonInfoPage(BasePage):
    def menu(self):
        # self.find(MobileBy.ID, 'com.tencent.wework:id/hvd').click()
        # self.find(MobileBy.ID, 'com.tencent.wework:id/b87').click()
        self.find_and_click(MobileBy.ID, 'com.tencent.wework:id/hvd')
        self.find_and_click(MobileBy.ID, 'com.tencent.wework:id/b87')
        return EditMemberPage(self.driver)