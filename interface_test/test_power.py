'''
Descripttion: 
version: 
Author: Liuwen
Date: 2021-11-29 10:07:57
LastEditTime: 2021-12-07 13:13:16
'''
from _pytest.mark import param
import pytest
from common.Request import Request
# import sys
# sys.path.append('F:\pytestdemo\demo_test')
from common.Readyaml import get_yaml_file
import requests
import logging
from string import Template
import json

class TestPower:
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger('power')
    

    @pytest.mark.parametrize('caseinfo',get_yaml_file('demo_test\\power\\find_allpower.yaml'))
    def test_find_allpower(self,caseinfo,get_token):
        name=caseinfo['name']
        header={'Authorization':get_token}
        methond=caseinfo['request']['methond']
        url=caseinfo['request']['url']
        data=caseinfo['request']['data']
        res=Request.session.request(method=methond,url=url,params=data,headers=header)
        # print(res.json())
        TestPower.power_id = res.json()['data'][-1]['id']
        assert caseinfo['validate']['code'] == res.json()['code']
        TestPower.log.info(f'查询所有电站响应：{res.json()}')
        
    @pytest.mark.parametrize('caseinfo',get_yaml_file('demo_test\\power\\find_powerbyid.yaml'))
    def test_find_powerbyid(self,caseinfo,get_token):
        name=caseinfo['name']
        header={'Authorization':get_token}
        methond=caseinfo['request']['methond']
        url=caseinfo['request']['url']+str(TestPower.power_id)
        data=caseinfo['request']['data']
        res=Request.session.request(method=methond,url=url,params=data,headers=header)
        assert caseinfo['validate']['code'] == res.json()['code']
        TestPower.log.info(f'根据电站id查询电站响应：{res.json()}')

    @pytest.mark.skip()
    @pytest.mark.parametrize('caseinfo',get_yaml_file('demo_test\\power\\findPowerCountGroupStatus.yaml'))
    def test_find_PowerCountGroupStatus(self,caseinfo,get_token):
        name=caseinfo['name']
        header={'Authorization':get_token}
        methond=caseinfo['request']['methond']
        url=caseinfo['request']['url']
        data=caseinfo['request']['data']
        res=Request.session.request(method=methond,url=url,params=data,headers=header)
        assert caseinfo['validate']['code'] == res.json()['code']
        TestPower.log.info(f'查询当前用户的正常和故障电站个数响应：{res.json()}')
        # print(res.json())

    # @pytest.mark.skip(reason='暂时不创建电站')
    # @pytest.mark.parametrize('caseinfo',get_yaml_file('demo_test\power\\device.yaml'))
    # def test_device_creat(self,caseinfo,login):
    #     header={'Authorization':login}
    #     name=caseinfo['name']
    #     methond=caseinfo['request']['methond']
    #     url=caseinfo['request']['url']
    #     data=caseinfo['request']['data']
    #     res=Request.session.request(method=methond,url=url,json=data,headers=header)
    #     print(res.json())