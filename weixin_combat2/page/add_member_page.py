from selenium.webdriver.common.by import By
from weixin_combat2.page.base_page import BasePage


class AddMemberPage(BasePage):

    # 给添加成员页面输入相应字段
    def add_member(self, name, id , tel):
        from weixin_combat2.page.contact_page import ContactPage
        self.find(By.ID, 'username').send_keys(name)
        self.find(By.ID, 'memberAdd_acctid').send_keys(id)
        self.find(By.ID, 'memberAdd_phone').send_keys(tel)

        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        return ContactPage()

    def get_field_massge(self):
        # self._field_message(By.CSS_SELECTOR, '#memberAdd_acctid+.ww_inputWithTips_tips').text
        # self._field_message(By.CSS_SELECTOR, '#username+.ww_inputWithTips_tips').text
        return self.find(By.CSS_SELECTOR, '.ww_telInput+.ww_inputWithTips_tips').text