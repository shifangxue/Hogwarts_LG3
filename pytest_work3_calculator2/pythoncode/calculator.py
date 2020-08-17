# 计算器的代码块，里面有加减乘除四个方法
class Calculator:
    
    def add(self, a, b):
        try:
            result = a + b
        except TypeError as e:
            print(f"输入的数值错误, \n {e} ")
            # 捕获到该异常后，重新抛出
            raise TypeError
        else:
            return result

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    """
        除法方法，如果b等于0时，手动抛出ZeroDivisionError
        如果输入不数值，捕获类型错误异常
    """
    def div(self, a, b):
        if b == 0:
            raise ZeroDivisionError()
        try:
            result = a / b
        except TypeError as e:
            print(f"输入的数值错误, \n {e} ")
            raise TypeError
        else:
            return round(result, 2)
