'''
Descripttion: 
version: 
Author: Liuwen
Date: 2021-11-24 11:12:05
LastEditTime: 2021-12-06 11:52:41
'''
import pytest
import requests

#使用fixture装饰器可以只对部分用例、类生效，
# autouse默认为false，当配置为true时，该方法/类都会执行
#scope=class时，在需要执行的class之前添加装饰器 @pytest.mark.usefixtures('exe_sql')
#scope=function时，在需要执行的方法参数中引入即可 def test_input(self,exe_sql):
@pytest.fixture(scope="class",autouse=False)
def exe_sql():
    print('用例执行之前,执行sql查询')
    yield  ##用例之后执行使用yield
    print('用例执行之后，执行sql并关闭数据库链接')

##数据驱动参数案例
def read_yaml():
    return ['zhangsan','lisi','wangwu']

@pytest.fixture(scope="function",params=read_yaml())
#request和request.param是固定写法
def exe_read(request):
    print('数据驱动测试：用例之前执行')
    yield request.param
    print('数据驱动测试：用例之后执行')

@pytest.fixture(scope="function",autouse=False)
def get_token():
    url = 'http://10.0.10.131/login?username=admin&password=1qaz!QAZ'
    method = 'post'
    data = {'name':'admin',
            'password':'1qaz!QAZ'
            }
    res = requests.post(url=url,json=data)
    return res.json()['data']['token']