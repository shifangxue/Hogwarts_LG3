"""
作业：编写删除联系人用例
思路：
    1.通讯录页面点击搜索按钮
    2.搜索页对象定义两个方法：存在的成员搜索、不存在的成员搜索
    3.不同的情况调用不同的方法实现删除和断言删除是否成功（或查找成员是否添加好友）
要求：将find_element/ click /send_keys / text 重新封装
"""
from app_combat2.page.main_page import MainPage


class TestDel:

    def setup(self):
        self.main = MainPage()

    def teardown(self):
        self.main.close()

    def test_del_member(self):
        search = self.main.go_to_contact().go_to_search()
        search.go_to_person('乔峰').menu().del_member()

        text = search.no_result('乔峰')
        assert '无搜索结果' == text

    def test_attribute(self):
        search = self.main.go_to_contact().go_to_search()
        print("is_displayed:", search.func("乔峰").is_displayed())
