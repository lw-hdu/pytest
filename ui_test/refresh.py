'''
Descripttion: 
version: 
Author: Liuwen
Date: 2021-11-23 09:50:27
LastEditTime: 2021-11-30 11:04:11
'''
import pytest
import sys
sys.path.append("F:\pytestdemo\common")
from test_common import CommonUnit

#@pytest.mark.skip(reason='无条件跳过')
class Test_02(CommonUnit):

    def test_02(self):
        print('refresh用例的第一个方法')

    @pytest.mark.smoke
    @pytest.mark.demo
    def test_002(self):
        print('refresh用例的第二个方法')