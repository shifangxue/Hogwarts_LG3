import shelve
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

"""
    使用浏览器复用，将微信登陆后的cookie进行持久化
        1.浏览器复用，获取登录的cookie
        2.对企业微信登录后cookie的持久化操作
        3.所有操作前提条件为登录，后续用例则在此条件下，对fixture的作用域设为session
"""


@pytest.fixture(scope="session")
def login():
    # 如果持久化文件不存在，则创建并增加cookie数据
    if not (os.path.exists("./mydb/logincookie.dat")):
        # 浏览器复用
        option = Options()
        option.debugger_address = "localhost:9222"
        driver = webdriver.Chrome(options=option)
        # driver.implicitly_wait(1)
        cookies = driver.get_cookies()
        f = shelve.open("./mydb/logincookie")
        f['cookie'] = cookies
        f.close()
