"""
创建微信登录页面PO
1. 通讯录页面
    返回通讯录页面对象
2. 添加成员页面
    返回添加成员页面对象
"""
from selenium.webdriver.common.by import By
from weixin_combat2.page.add_member_page import AddMemberPage
from weixin_combat2.page.base_page import BasePage
from weixin_combat2.page.contact_page import ContactPage

# 继承BasePage类，复用webdriver对象、查找元素方法
class MainPage(BasePage):

    def go_to_contact(self):
        # 点击通讯选项
        self.find(By.CSS_SELECTOR, '#menu_contacts').click()
        return ContactPage(self.driver)

    def go_to_member(self):
        # 点击添加成员按钮
        self.find(By.CSS_SELECTOR, '[node-type="addmember"]').click()
        return AddMemberPage(self.driver)