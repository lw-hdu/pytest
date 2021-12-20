'''
Descripttion: 
Author: Liuwen
Date: 2021-12-20 09:09:12
LastEditTime: 2021-12-20 10:00:21
'''
from test_request import TestRequest 

class TestLongi:
    tr = TestRequest(r'F:\pytestdemo\demo_test\power\find_allpower.yaml')
    tr.test_device()