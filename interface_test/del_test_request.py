'''
Descripttion: 
version: 
Author: Liuwen
Date: 2021-12-01 15:01:13
LastEditTime: 2021-12-01 16:48:45
'''
from os import listdir 
from _pytest.mark import param
import pytest
from common.Request import Request
from common.Readyaml import get_yaml_file


class TestRequest:
    # device_file = listdir('F:\pytestdemo\demo_test\device')
    # # print(device_file)
    # for i in device_file:
    #     print(f'获取到的文件名为{i}')
    @pytest.mark.parametrize('caseinfo',get_yaml_file('demo_test\\device\\create_device.yaml'))
    # @pytest.mark.parametrize('caseinfo',get_yaml_file('demo_test\\device\\delete_device.yaml'))
    # @pytest.mark.parametrize('caseinfo',get_yaml_file('demo_test\\device\\find_devicebytype.yaml'))
    def test_device(self,caseinfo,login):
        name=caseinfo['name']
        header={'Authorization':login}
        methond=caseinfo['request']['methond']
        url=caseinfo['request']['url']
        data=caseinfo['request']['data']
        if methond.lower() == 'get':
            res=Request.session.request(method=methond,url=url,json=data,headers=header)
        elif methond.lower() == 'post':
            res=Request.session.request(method=methond,url=url,json=data,headers=header)

            assert caseinfo['validate']['code'] == res.json()['code']
            assert caseinfo['validate']['msg'] == res.json()['msg']
            

