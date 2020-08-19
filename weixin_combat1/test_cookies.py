import shelve
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

"""
作业：使用cookie 登录企业微信，完成导入联系人，加上断言验证
1.将cookie信息持久化，并放入fixture中
2.增加浏览器配置，以加快浏览器启动速度
3.执行用例：进入企业微信页面，并上传excel通讯录文件，并断言是否上传成功
4.关闭浏览，并在1秒后清除进程
"""
class TestWeiXin:

    def setup(self):
        # 设置浏览器配置，增加打开速度
        option = Options()
        option.add_argument("--disable-inforbars")
        option.add_argument("--start-maximized")
        option.add_experimental_option('excludeSwitches',['enable-automation'])
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(3)

    def teardown(self):
        # 关闭浏览器1秒后，开始执行清理selenium进程
        self.driver.quit()
        time.sleep(1)
        self.driver.__exit__()

    def test_cookies(self, login):
        # 强制等待，在cookie持久化操作之后
        time.sleep(3)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        f = shelve.open("./mydb/logincookie")
        self.cookies = f['cookie']
        for cookie in self.cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # 进入导入通讯录选项
        self.driver.find_element_by_xpath("//span[contains(.,'导入通讯录')]").click()
        # 上传一个xls文件
        upload = self.driver.find_element_by_xpath("//input[@id='js_upload_file_input']")
        upload.send_keys("d:/connect.xlsx")
        # 断言文件是否上传成功
        assert "connect" in self.driver.find_element_by_id("upload_file_name").text

        time.sleep(3)

