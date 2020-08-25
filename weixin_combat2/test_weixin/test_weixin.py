"""
作业：使用po思想完成添加部门操作的自动化测试（注意组合定位）

"""
import pytest
import yaml
from time import sleep
from weixin_combat2.page.add_member_page import AddMemberPage
from weixin_combat2.page.contact_page import ContactPage
from weixin_combat2.page.main_page import MainPage


class TestWeixin:

    # _expecteds = ['请填写姓名','请填写正确的手机号码','请填写帐号','该帐号已被“沙邦”占有']

    def setup(self):
        self.main = MainPage()

    def teardown(self):
        self.main.driver.quit()

    # 添加部门用例
    @pytest.mark.parametrize("depart", ['产品部','销售部'])
    def test_add_depart(self, depart):
        self.main.go_to_contact().go_to_add_depart().add_depart(depart)
        sleep(1)
        result = ContactPage(self.main.driver).get_depart_list()
        assert depart in result

    """
    打开通讯录页面-->点击添加成员
    断言成员是否添加
    """
    @pytest.mark.parametrize("name,id,tel", yaml.safe_load(open("../data/members.yml", encoding='utf-8')))
    def test_add_contact(self, name, id, tel):
        results = self.main.go_to_contact().go_to_add_member().add_member(name, id, tel).get_member_list()
        assert name in results

    @pytest.mark.parametrize('name,id,tel',(['BD','killer002','1440001444a'],['','','']))
    def test_add_contact_fail(self, name, id, tel):
        self.main.go_to_contact().go_to_add_member().add_member(name,id,tel)
        result = AddMemberPage(self.main.driver).get_field_massge()
        assert '请填写正确的手机号码' == result

    @pytest.mark.parametrize("name,id,tel", yaml.safe_load(open("../data/members.yml", encoding='utf-8')))
    def test_add_member(self, name, id, tel):
        result = self.main.go_to_member().add_member(name, id ,tel).get_member_list()
        assert name in result

    @pytest.mark.parametrize('name,id,tel', (['BD', 'killer002', '1440001444a'], ['', '', '']))
    def test_add_member_fail(self, name, id, tel):
        self.main.go_to_member().add_member(name, id, tel)
        result = AddMemberPage(self.main.driver).get_field_massge()
        assert '请填写正确的手机号码' == result