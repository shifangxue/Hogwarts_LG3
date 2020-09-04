from app_combat1.page.main_page import MainPage


class TestAdd:

    def setup(self):
        self.main = MainPage()

    def teardown(self):
        self.main.close()

    def test_manual_input(self):
        ele = self.main.go_to_contact().go_to_add_member().go_to_manual_input().add_member('乔峰', '男', '15516601001')
        assert ele.text == "添加成功"

