'''
Descripttion: 
version: 
Author: Liuwen
Date: 2021-12-01 10:53:32
LastEditTime: 2021-12-07 17:04:51
'''
from _pytest.mark import param
import pytest
from common.Request import Request
from common.Readyaml import get_yaml_file
import allure
import logging

class TestCommand:
    command_id=''
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger('command')

    @allure.title('创建命令')
    @pytest.mark.parametrize('caseinfo',get_yaml_file('demo_test\\command\\create_command.yaml'))
    def test_create_command(self,caseinfo,get_token):
        name=caseinfo['name']
        header={'Authorization':get_token}
        methond=caseinfo['request']['methond']
        url=caseinfo['request']['url']
        data=caseinfo['request']['data']
        res=Request.session.request(method=methond,url=url,json=data,headers=header)
        assert caseinfo['validate']['code'] == res.json()['code']
        assert caseinfo['validate']['msg'] == res.json()['msg']
        TestCommand.log.info(f'执行的测试用例名称：{name}')
        TestCommand.log.info(f'创建命令响应：{res.json()}')

    
    @allure.title('查询命令')
    @pytest.mark.parametrize('caseinfo',get_yaml_file('demo_test\\command\\find_commandpage.yaml'))
    def test_find_command(self,caseinfo,get_token):
        name=caseinfo['name']
        header={'Authorization':get_token}
        methond=caseinfo['request']['methond']
        url=caseinfo['request']['url']
        data=caseinfo['request']['data']
        res=Request.session.request(method=methond,url=url,params=data,headers=header)
        TestCommand.command_id=res.json()['data']['content'][0]['id']
        assert caseinfo['validate']['code'] == res.json()['code']
        assert caseinfo['validate']['msg'] == res.json()['msg']
        TestCommand.log.info(f'执行的测试用例名称：{name}')
        TestCommand.log.info(f'查询命令响应结果:{res.json()}')

    
    @allure.title('删除命令')
    @pytest.mark.parametrize('caseinfo',get_yaml_file('demo_test\\command\\delete_command.yaml'))
    def test_del_command(self,caseinfo,get_token):
        name=caseinfo['name']
        header={'Authorization':get_token}
        methond=caseinfo['request']['methond']
        url=caseinfo['request']['url']+str(TestCommand.command_id)
        data=caseinfo['request']['data']
        res=Request.session.request(method=methond,url=url,params=data,headers=header)
        assert caseinfo['validate']['code'] == res.json()['code']
        assert caseinfo['validate']['msg'] == res.json()['msg']
        TestCommand.log.info(f'执行的测试用例名称：{name}')
        TestCommand.log.info(f'删除的命令id为：{TestCommand.command_id}')
        TestCommand.log.info(f'删除命令响应：{res.json()}')