from appium.webdriver.common.mobileby import MobileBy

from app_combat1.page.base_page import BasePage
from app_combat1.page.person_info_page import PersonInfoPage


class SearchPage(BasePage):

    def go_to_person(self, name):
        # 搜索框输入成员名称
        self.find(MobileBy.ID, 'com.tencent.wework:id/gfs').send_keys(name)
        self.find(MobileBy.ID, 'com.tencent.wework:id/gfs').click()
        # 如果搜索的成员存在，点击该成员
        t1 = self.find(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/hqj' and @text='联系人']").text

        n = '//*[@class="android.widget.TextView" and @text=\"'+name+'\"]'
        self.find(MobileBy.XPATH, n).click()
        return PersonInfoPage(self.driver)

    def no_result(self, name):
        return self.find(MobileBy.ID, 'com.tencent.wework:id/c_0').text
