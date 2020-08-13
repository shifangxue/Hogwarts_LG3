"""
作业
1、补全计算器（加法 除法）的测试用例
2、使用参数化完成测试用例的自动生成
3、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】

注意：
使用等价类，边界值，因果图等设计测试用例
测试用例中添加断言，验证结果
灵活使用 setup(), teardown() , setup_class(), teardown_class()
"""
import pytest
import yaml
from pytest_work3_calculator.pythoncode.calculator import Calculator


def get_value(k1, k2):
    with open("./data.yml") as f:
        allData = yaml.safe_load(f)
        return allData[k1][k2]

class TestCase:

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("计算结束")

    def setup_class(self):
        self.cal = Calculator()

    def teardown_class(self):
        del self.cal

    """测试整形数据相加"""
    @pytest.mark.parametrize(["a", "b", "expected"], get_value("add", "intdatas"))
    def test_add_int(self, a, b, expected):
        actual = self.cal.add(a, b)
        assert actual == expected, f"实际结果{actual}与预期结果不一致{expected}"

    """测试浮点型数字相加"""
    @pytest.mark.parametrize("a, b, expected", get_value("add", "floatdatas"))
    def test_add_float(self, a, b, expected):
        actual = self.cal.add(a, b)
        assert actual == expected, f"实际结果{actual}与预期结果不一致{expected}"

    """测试输入非数字值时，是否抛出TypeError异常"""
    @pytest.mark.parametrize("a, b",get_value("add", "raisevalue"))
    def test_add_raise(self, a, b):
        with pytest.raises(TypeError) as e:
            self.cal.add(a, b)

    @pytest.mark.parametrize("a, b, expected", get_value("div", "intdatas"))
    def test_div_int(self, a, b, expected):
        actual = self.cal.div(a, b)
        assert actual == expected, f"实际结果{actual}与预期结果不一致{expected}"

    @pytest.mark.parametrize("a, b, expected", get_value("div", "floatdatas"))
    def test_div_float(self, a, b, expected):
        actual = self.cal.div(a, b)
        assert actual == expected, f"实际结果{actual}与预期结果不一致{expected}"

    """测试被0除时，是否抛出ZeroDivisionError异常"""
    @pytest.mark.parametrize("a, b",get_value("div", "raisevalue"))
    def test_div_raise(self, a, b):
        with pytest.raises((ZeroDivisionError, TypeError)) as e:  # 断言预期的异常可以处理多个，参数为tuple类型
            self.cal.div(a, b)