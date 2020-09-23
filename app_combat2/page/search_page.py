from appium.webdriver.common.mobileby import MobileBy

from app_combat2.page.base_page import BasePage
from app_combat2.page.person_info_page import PersonInfoPage


class SearchPage(BasePage):

    def go_to_person(self, name):
        # 搜索框输入成员名称
        # self.find(MobileBy.ID, 'com.tencent.wework:id/gfs').send_keys(name)
        # self.find(MobileBy.ID, 'com.tencent.wework:id/gfs').click()
        self.find_and_sendKeys(MobileBy.ID, 'com.tencent.wework:id/gfs', name)
        self.find_and_click(MobileBy.ID, 'com.tencent.wework:id/gfs')
        # 如果搜索的成员存在，点击该成员，进入成员编辑页
        # t1 = self.find(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/hqj' and @text='联系人']").text
        n = '//*[@class="android.widget.TextView" and @text=\"'+name+'\"]'
        # self.find(MobileBy.XPATH, n).click()

        self.find_and_click(MobileBy.XPATH, n)
        return PersonInfoPage(self.driver)

    # 搜索的成员不存在
    def no_result(self, name):
        self.find_and_sendKeys(MobileBy.ID, 'com.tencent.wework:id/gfs', name)
        self.find_and_click(MobileBy.ID, 'com.tencent.wework:id/gfs')
        return self.find_and_getText(MobileBy.ID, 'com.tencent.wework:id/c_0')

    def func(self, name):
        self.find_and_sendKeys(MobileBy.ID, 'com.tencent.wework:id/gfs', name)
        self.find_and_click(MobileBy.ID, 'com.tencent.wework:id/gfs')
        n = '//*[@class="android.widget.TextView" and @text=\"' + name + '\"]'
        return self.find(MobileBy.XPATH, n)
