from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from app_combat1.page.base_page import BasePage


class ManualInputPage(BasePage):

    def add_member(self, name, gender, phone):
        print("ManualInputPage, add_member")
        self.find(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/b2i' and  @text='必填']").send_keys(name)
        self.find(MobileBy.ID, 'com.tencent.wework:id/fh_').send_keys(phone)
        self.find(MobileBy.XPATH, '//*[@text="男"]').click()
        if gender == '男':
            self.find(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/eas' and @text='男']").click()
        else:
            self.find(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/eas' and @text='女']").click()

        self.find(MobileBy.ID, 'com.tencent.wework:id/hvk').click()
        # sleep(2)
        # print(self.driver.page_source)
        return self.find(MobileBy.XPATH, '//*[@class="android.widget.Toast"]')
