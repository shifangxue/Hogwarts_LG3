"""
作业2：
1、编写用例顺序：加- 除-减-乘
2、控制测试用例顺序按照【加-减-乘-除】这个顺序执行
3、本地生成测试报告

本次测试使用pytest-ordering插件控制用例的执行顺序
    @pytest.mark.run(order=ordernum)
    每个测试方法分别使用不同类型的有效与无效等价划分取值，控制用例执行顺序为加减乘除
"""
import pytest
from pytest_work3_calculator2.conftest import get_datas
from pytest_work3_calculator2.pythoncode.calculator import Calculator


class TestCal:

    # 测试用例使用的测试对象作用域只在本类对象范围，不设定在conftest.py中
    def setup_class(self):
        self.cal = Calculator()

    def teardown_class(self):
        del self.cal

    # 测试整形数据相加
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize(["a", "b", "expected"], get_datas("add", "intdatas"))
    def test_add_int(self, a, b, expected):
        print("test_add_int")
        actual = self.cal.add(a, b)
        assert actual == expected, f"实际结果{actual}与预期结果不一致{expected}"

    # 测试浮点型数字相加
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("a, b, expected", get_datas("add", "floatdatas"))
    def test_add_float(self, a, b, expected):
        print("test_add_float")
        actual = self.cal.add(a, b)
        assert actual == expected, f"实际结果{actual}与预期结果不一致{expected}"

    # 测试输入非数字值时，是否抛出TypeError异常
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("a, b", get_datas("add", "raisevalue"))
    def test_add_raise(self, a, b):
        print("test_add_raise")
        with pytest.raises(TypeError):
            self.cal.add(a, b)

    # 除法测试用例
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("a, b, expected", get_datas("div", "intdatas"))
    def test_div_int(self, a, b, expected):
        print("test_div_int")
        actual = self.cal.div(a, b)
        assert actual == expected, f"实际结果{actual}与预期结果不一致{expected}"

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("a, b, expected", get_datas("div", "floatdatas"))
    def test_div_float(self, a, b, expected):
        print("test_div_float")
        actual = self.cal.div(a, b)
        assert actual == expected, f"实际结果{actual}与预期结果不一致{expected}"

    """测试被0除时，是否抛出ZeroDivisionError异常"""
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("a, b", get_datas("div", "raisevalue"))
    def test_div_raise(self, a, b):
        print("test_div_raise")
        with pytest.raises((ZeroDivisionError, TypeError)):  # 断言预期的异常可以处理多个，参数为tuple类型
            self.cal.div(a, b)

    # 减法测试用例--整型运算
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("a, b, expected", get_datas("sub", "intdatas"))
    def test_sub_int(self, a, b, expected):
        print("test_sub_int")
        result = self.cal.sub(a, b)
        assert result == expected

    # 减法测试用例--浮点型运算（使用round四舍五入取小数点后两位）
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("a, b, expected", get_datas("sub", "floatdatas"))
    def test_sub_float(self, a, b, expected):
        print("test_sub_int")
        result = self.cal.sub(a, b)
        assert round(result, 2) == expected

    # 减法测试用例--整型与字符运算，测试是否会抛出TypeError
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("a, b", get_datas("sub", "raisevalue"))
    def test_sub_raise(self, a, b):
        print("test_sub_int")
        with pytest.raises(TypeError):
            self.cal.sub(a, b)

    # 乘法测试用例——整型及与字符的相乘运算
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("a, b, expected", get_datas("mul", "intdatas"))
    def test_mul_int(self, a, b, expected, tobeornottobe):
        print("test_mul_int")
        result = self.cal.mul(a, b)
        assert result == expected

    # 乘法测试用例——浮点型及与字符的相乘运算
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("a, b, expected", get_datas("mul", "floatdatas"))
    def test_mul_float(self, a, b, expected):
        print("test_mul_float")
        result = self.cal.mul(a, b)
        assert round(result, 2) == expected

    # 乘法测试用例——整型、浮点型和字符的相乘运算
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("a, b", get_datas("mul", "raisevalue"))
    def test_mul_raise(self, a, b):
        print("test_mul_raise")
        with pytest.raises(TypeError):
            self.cal.mul(a, b)
