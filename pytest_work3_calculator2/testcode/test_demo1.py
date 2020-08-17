"""
作业1：
1、补全计算器（加减乘除）的测试用例
2、创建 Fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】
3、将 Fixture 方法存放在conftest.py ，设置scope=module

本次测试补充乘法与减法测试用例
    使用类级别的setup与teardown方法实例化测试对象并最终删除测试对象
    使用conftest.py配置文件将module、方法级别的fixture放入其中
    参数化读取函数放置conftest.py中
    两个测试方法的参数取值分别为整型、浮点型及与字符相互运算
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

    # 乘法测试用例——整型及与字符的相乘运算
    @pytest.mark.parametrize("a, b, expected", get_datas("mul", "intdatas"))
    def test_mul_int(self, a, b, expected, tobeornottobe):
        print("test_mul_int")
        result = self.cal.mul(a, b)
        assert result == expected

    # 乘法测试用例——浮点型及与字符的相乘运算
    @pytest.mark.parametrize("a, b, expected", get_datas("mul", "floatdatas"))
    def test_mul_float(self, a, b, expected):
        print("test_mul_float")
        result = self.cal.mul(a, b)
        assert round(result, 2) == expected

    # 乘法测试用例——整型、浮点型和字符的相乘运算
    @pytest.mark.parametrize("a, b", get_datas("mul", "raisevalue"))
    def test_mul_raise(self, a, b):
        print("test_mul_raise")
        with pytest.raises(TypeError):
            self.cal.mul(a, b)

    # 减法测试用例--整型运算
    @pytest.mark.parametrize("a, b, expected", get_datas("sub", "intdatas"))
    def test_sub_int(self, a, b, expected):
        print("test_sub_int")
        result = self.cal.sub(a, b)
        assert result == expected

    # 减法测试用例--浮点型运算（使用round四舍五入取小数点后两位）
    @pytest.mark.parametrize("a, b, expected", get_datas("sub", "floatdatas"))
    def test_sub_float(self, a, b, expected):
        print("test_sub_int")
        result = self.cal.sub(a, b)
        assert round(result, 2) == expected

    # 减法测试用例--整型与字符运算，测试是否会抛出TypeError
    @pytest.mark.parametrize("a, b", get_datas("sub", "raisevalue"))
    def test_sub_raise(self, a, b):
        print("test_sub_int")
        with pytest.raises(TypeError):
            self.cal.sub(a, b)

