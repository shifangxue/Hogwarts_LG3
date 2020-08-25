from selenium.webdriver.common.by import By

from weixin_combat2.page.base_page import BasePage


class AddDepartPage(BasePage):

    def add_depart(self, depart):
        # 输入部门名称
        self.find(By.CSS_SELECTOR, 'form.form div.inputDlg_item input.ww_inputText[name="name"]').send_keys(depart)
        # 点击所属部门
        self.find(By.CSS_SELECTOR, 'form.form div.inputDlg_item a.js_toggle_party_list').click()
        # 选择部门
        self.find(By.CSS_SELECTOR, 'form.form div.inputDlg_item div.js_party_list_container div.jstree-default ul.jstree-no-dots li.jstree-last a.jstree-anchor').click()
        self.find(By.CSS_SELECTOR, 'div.member_tag_dialog .ww_btn_Blue[d_ck="submit"]').click()