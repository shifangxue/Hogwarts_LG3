from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from app_combat2.page.base_page import BasePage


class ManualInputPage(BasePage):

    def add_member(self, name, gender, phone):
        # self.find(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/b2i' and  @text='必填']").send_keys(name)
        # self.find(MobileBy.ID, 'com.tencent.wework:id/fh_').send_keys(phone)
        # self.find(MobileBy.XPATH, '//*[@text="男"]').click()
        self.find_and_sendKeys(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/b2i' and  @text='必填']", name)
        self.find_and_sendKeys(MobileBy.ID, 'com.tencent.wework:id/fh_', phone)
        self.find_and_click(MobileBy.XPATH, '//*[@text="男"]')
        if gender == '男':
            # self.find(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/eas' and @text='男']").click()
            self.find_and_click(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/eas' and @text='男']")
        else:
            # self.find(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/eas' and @text='女']").click()
            self.find_and_click(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/eas' and @text='女']")

        # self.find(MobileBy.ID, 'com.tencent.wework:id/hvk').click()
        self.find_and_click(MobileBy.ID, 'com.tencent.wework:id/hvk')
        # sleep(2)
        # print(self.driver.page_source)
        return self.find(MobileBy.XPATH, '//*[@class="android.widget.Toast"]')
