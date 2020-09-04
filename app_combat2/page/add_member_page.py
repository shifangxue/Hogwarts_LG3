from appium.webdriver.common.mobileby import MobileBy

from app_combat2.page.base_page import BasePage
from app_combat2.page.manual_input_page import ManualInputPage


class AddMemberPage(BasePage):

    # 手动输入添加成员
    def go_to_manual_input(self):
        # 点击手动输入添加，转向添加成员页
        print("AddMemberPage, find")
        # self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.find_and_click(MobileBy.XPATH, "//*[@text='手动输入添加']")
        return ManualInputPage(self.driver)

    # 微信邀请同事
    def go_to_invitation(self):
        pass

    # 微信/手机通讯录中添加
    def go_to_phone_invitation(self):
        pass
