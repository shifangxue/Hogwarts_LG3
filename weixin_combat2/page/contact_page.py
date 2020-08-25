"""
创建通讯录页面对象
1.添加成员
    返回添加成员页面对象
2.添加部门
    返回添加部门页面对象
"""
from time import sleep
from selenium.webdriver.common.by import By
from weixin_combat2.page.add_depart_page import AddDepartPage
from weixin_combat2.page.add_member_page import AddMemberPage
from weixin_combat2.page.base_page import BasePage


class ContactPage(BasePage):

    def go_to_add_member(self):
        # 点击通讯录页面中的添加成员按钮
        sleep(1)
        self.find(By.CSS_SELECTOR, '.ww_operationBar .js_add_member').click()
        return AddMemberPage(self.driver)

    def go_to_add_depart(self):
        self.find(By.CSS_SELECTOR, '.js_create_dropdown').click()
        self.find(By.CSS_SELECTOR, '.js_create_dropdown_container li a.js_create_party').click()
        return AddDepartPage(self.driver)

    def get_member_list(self):
        list1 = []
        member_list = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        for member in member_list:
            list1.append(member.text)
        print(list1)
        return list1

    def get_depart_list(self):
        departs = self.finds(By.CSS_SELECTOR, '.jstree-no-dots[role="group"] .jstree-open a')
        list1 = []
        for depart in departs:
            list1.append(depart.text)
        return list1