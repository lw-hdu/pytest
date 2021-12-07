'''
Descripttion: 
version: 
Author: Liuwen
Date: 2021-11-22 19:42:57
LastEditTime: 2021-11-26 17:01:14
'''
import pytest
import sys
sys.path.append("F:\pytestdemo\common")

from test_common import CommonUnit


i=19

class Test_01(CommonUnit):
        
    @pytest.mark.skipif(i>10,reason='i<=10时执行该用例')    
    def test_01(self):
        print('一个类中的第一个函数')

    #@pytest.mark.skip(reason='无理由跳过')
    def test_001(self,exe_sql):
        print('一个类中的第二个函数')

class Test_001(CommonUnit):

    def test_apple(self):
        print('第二个类的第一个函数')





