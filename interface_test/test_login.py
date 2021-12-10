'''
Descripttion: 
version: 
Author: Liuwen
Date: 2021-11-29 10:07:57
LastEditTime: 2021-12-09 11:45:50
'''
import pytest
from common.Request import Request
from common.Readyaml import get_yaml_file
import allure
import logging
#从其他测试用例中引入参数id
# from interface_test.test_device import TestDevice

class TestLongi:

    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger('user_login')

    @allure.title('登录测试')
    @pytest.mark.parametrize('caseinfo',get_yaml_file('demo_test\\login.yaml'))
    def test_login(self,caseinfo):
        name=caseinfo['name']
        methond=caseinfo['request']['methond']
        url=caseinfo['request']['url']
        data=caseinfo['request']['data']
        res=Request.session.request(method=methond,url=url,json=data)
        assert caseinfo['validate']['code'] == res.json()['code']
        assert caseinfo['validate']['msg'] == res.json()['msg']
        TestLongi.log.info(f'执行的测试用例名称：{name}')
        TestLongi.log.info(f'登录请求body:{data}')
        TestLongi.log.info(f'登录的响应结果： {res.json()}')

        #从其他测试用例中引入参数id
        # id = TestDevice.device_id
        # print(id)
