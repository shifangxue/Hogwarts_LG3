from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from app_combat2.page.base_page import BasePage


class EditMemberPage(BasePage):
    def del_member(self):
        # self.find(MobileBy.ID, 'com.tencent.wework:id/efq').click()
        self.find_and_click(MobileBy.ID, 'com.tencent.wework:id/efq')
        sleep(1)
        # self.find(MobileBy.ID, 'com.tencent.wework:id/bit').click()
        self.find_and_click(MobileBy.ID, 'com.tencent.wework:id/bit')
        sleep(2)
