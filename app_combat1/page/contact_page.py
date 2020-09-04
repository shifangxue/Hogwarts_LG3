from appium.webdriver.common.mobileby import MobileBy

from app_combat1.page.add_member_page import AddMemberPage
from app_combat1.page.base_page import BasePage
from app_combat1.page.search_page import SearchPage


class ContactPage(BasePage):

    def go_to_add_member(self):
        # 通讯录页面点击添加成员，转向添加成员页
        self.find(MobileBy.XPATH, "//*[@text='添加成员']").click()
        return AddMemberPage(self.driver)

    def go_to_search(self):
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/hvn').click()
        return SearchPage(self.driver)
