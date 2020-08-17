import os
import pytest
import yaml

# 根据需求，fixture updown 方法每个测试用例都需执行，设置 autouse=True
@pytest.fixture(scope="function", autouse=True)
def updown():
    print("开始计算")
    yield
    print("计算结束")

@pytest.fixture(scope="module")
def tobeornottobe():
    print("测试用例开始执行")
    yield
    print("测试工作结束")

def get_datas(k1, k2):
    datapath = os.path.dirname(__file__)
    with open(datapath+"/datas.yml", encoding='utf-8') as f:
        mydatas = yaml.safe_load(f)
        v = mydatas[k1][k2]
        return v

