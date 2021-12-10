'''
Descripttion: 
Author: Liuwen
Date: 2021-12-10 08:40:53
LastEditTime: 2021-12-10 10:16:50
'''
class Test1:
    def __init__(self,path) -> None:
        self.path = path

    def test_print(self,value):
        print(f'打印参数{self.path},函数的参数{value}')