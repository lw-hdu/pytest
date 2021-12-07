'''
Descripttion: 
version: 
Author: Liuwen
Date: 2021-12-01 10:53:32
LastEditTime: 2021-12-07 13:12:14
'''
'''
Descripttion: 
version: 
Author: Liuwen
Date: 2021-11-29 10:07:57
LastEditTime: 2021-12-01 14:51:22
'''
from _pytest.mark import param
import pytest
from common.Request import Request
from common.Readyaml import get_yaml_file
import allure
import logging
import json
from string import Template

class TestDevice:
    device_id=''
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger('device')

    @allure.title('创建设备')
    @pytest.mark.parametrize('caseinfo',get_yaml_file('demo_test\\device\\create_device.yaml'))
    def test_create_device(self,caseinfo,get_token):
        name=caseinfo['name']
        header={'Authorization':get_token}
        methond=caseinfo['request']['methond']
        url=caseinfo['request']['url']
        data=caseinfo['request']['data']
        res=Request.session.request(method=methond,url=url,json=data,headers=header)
        assert caseinfo['validate']['code'] == res.json()['code']
        assert caseinfo['validate']['msg'] == res.json()['msg']
        TestDevice.log.info(f'创建设备响应{res.json()}')
        

    @allure.title('查询设备')
    @pytest.mark.parametrize('caseinfo',get_yaml_file('demo_test\\device\\find_devicebytype.yaml'))
    def test_find_device(self,caseinfo,get_token):
        name=caseinfo['name']
        header={'Authorization':get_token}
        methond=caseinfo['request']['methond']
        url=caseinfo['request']['url']
        data=caseinfo['request']['data']
        res=Request.session.request(method=methond,url=url,params=data,headers=header)
        TestDevice.device_id = str(res.json()['data']['content'][0]['id'])
        assert caseinfo['validate']['code'] == res.json()['code']
        assert caseinfo['validate']['msg'] == res.json()['msg']
        TestDevice.log.info(f'查询pytest自动化测试专用电站下设备响应：{res.json()}')

    @allure.title('删除设备')
    @pytest.mark.parametrize('caseinfo',get_yaml_file('demo_test\\device\\delete_device.yaml'))
    def test_del_device(self,caseinfo,get_token):
        #初始化，通过json.dumps()将json格式的测试用例转换为str
        temp = Template(json.dumps(caseinfo))
        #yaml文件中id参数的取值
        d = {
            'id':TestDevice.device_id,
            'id_null':999999
            }
        #将id的值传入yaml的$id字段，并通过json.loads()将str转换为dict
        case = json.loads(temp.safe_substitute(d))
        header={'Authorization':get_token}
        name=case['name']
        methond=case['request']['methond']
        url=case['request']['url']
        data=case['request']['data']
        res=Request.session.request(method=methond,url=url,params=data,headers=header)
        TestDevice.log.info(f'执行的测试用例名称：{name}')
        TestDevice.log.info(f'删除请求url:{url}')
        TestDevice.log.info(f'删除设备响应：{res.json()}')