import pytest
import yaml

from app_combat2.page.main_page import MainPage
from app_combat2.test_case.read import read_data


class TestAdd:

    def setup(self):
        self.main = MainPage()

    def teardown(self):
        self.main.close()

    @pytest.mark.parametrize("name,gender,phone", read_data())
    def test_manual_input(self, name, gender, phone):
        ele = self.main.go_to_contact().go_to_add_member().go_to_manual_input().add_member(name, gender, phone)
        assert ele.text == "添加成功"

