import requests

"""
部门管理页面
1。创建部门
2。更新部门
3。删除部门
4。查看部门
"""

class DepartmentManager:
    _corpid = "wwe746196a9fb7d20a"
    _corpsecret = "VDz6_6BAPXkjl-ebl0n2ptEg5QDJhDbXh8ekHru_GoE"
    base_host = "https://qyapi.weixin.qq.com/"
    _token = ""

    def __init__(self):
        uri = f'cgi-bin/gettoken?corpid={self._corpid}&corpsecret={self._corpsecret}'
        r = requests.get(self.base_host+uri)
        self._token = r.json()['access_token']

    # 提供获取token接口
    def get_token(self):
        return self._token

    # 创建部门
    def add_department(self, data):
        uri = f'cgi-bin/department/create?access_token={self._token}'
        r = requests.post(self.base_host+uri, json=data)
        return r.json()['errmsg']

    def update_department(self, data):
        uri = f'cgi-bin/department/update?access_token={self._token}'
        r = requests.post(self.base_host+uri, json=data)
        return r.json()['errmsg']

    def get_department(self):
        uri = f'cgi-bin/department/list?access_token={self._token}'
        r = requests.get(self.base_host+uri)
        return r.json()

    def del_department(self, userid):
        uri = f'cgi-bin/department/delete?access_token={self._token}&id={userid}'
        r = requests.get(self.base_host+uri)
        return r.json()['errmsg']
