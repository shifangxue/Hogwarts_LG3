from weixin_requests1.page.department_manager import DepartmentManager


class TestDepartment:

    def setup_class(self):
        self.department_manager = DepartmentManager()

    def test_add_department(self):
        data = {
            "parentid": 2,
            "name": "行政部",
            "id": 4
        }
        actual = self.department_manager.add_department(data)
        assert actual == 'created'

    def test_update_department(self):
        data = {
            "parentid": 2,
            "name": "总经办",
            "id": 4,
            "order": 200000000
        }
        actual = self.department_manager.update_department(data)
        assert actual == 'updated'

    def test_del_department(self):
        userid = 4
        actual = self.department_manager.del_department(userid)
        assert actual == 'deleted'

    def test_get_department(self):
        json_obj = self.department_manager.get_department()
        department_list = json_obj['department']
        print(department_list)
        assert json_obj['errmsg'] == 'ok'
