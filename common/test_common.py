'''
Descripttion: 
version: 
Author: Liuwen
Date: 2021-11-23 17:22:17
LastEditTime: 2021-11-24 09:20:52
'''

from selenium import webdriver

class CommonUnit:
    def setup(self):
        print('每个用例执行之前执行')

    def teardown(self):
        print('每个用例执行之后执行')

    def setup_class(self):
        print('每个class之前执行')

    def teardown_class(self):
        print('每个class之后执行')