'''
Descripttion: 
Author: Liuwen
Date: 2021-12-17 17:26:56
LastEditTime: 2021-12-20 17:01:57
'''
import pytest
from common.Request import Request
from RYaml import get_yaml_file
import logging


# class TestRequest:
#     file_path = ''

#     def __init__(self,path) -> None:
#         self.file_path = path

#     @pytest.mark.parametrize('caseinfo',get_yaml_file(file_path))
#     def test_request(self,caseinfo,get_token):
#         name=caseinfo['name']
#         header={'Authorization':get_token}
#         methond=caseinfo['request']['methond']
#         url=caseinfo['request']['url']
#         data=caseinfo['request']['data']
#         if methond.lower() == 'get':
#             res=Request.session.request(method=methond,url=url,params=data,headers=header)
#         elif methond.lower() == 'post':
#             res=Request.session.request(method=methond,url=url,json=data,headers=header)
        
#             assert caseinfo['validate']['code'] == res.json()['code']
#             assert caseinfo['validate']['msg'] == res.json()['msg']

# tr = TestRequest('F:\\pytestdemo\\demo_test\\power\\find_allpower.yaml')
# tr.test_request()


all_file = [
            'F:\\pytestdemo\\demo_test\\power\\create_power.yaml',
            'F:\\pytestdemo\\demo_test\\login.yaml',
            'F:\\pytestdemo\\demo_test\\command\\find_commandpage.yaml'
            ]
for i in range(len(all_file)):
    @pytest.mark.parametrize('caseinfo',get_yaml_file(all_file[i]))
    def test_request(caseinfo,get_token):
        logging.basicConfig(level=logging.INFO)
        log = logging.getLogger()
        name=caseinfo['name']
        header={'Authorization':get_token}
        methond=caseinfo['request']['methond']
        url=caseinfo['request']['url']
        data=caseinfo['request']['data']
        log.info(f'这是第{i+1}个文件')
        log.info(f'执行的测试用例名称：{name}')
        if methond.lower() == 'get':
            res=Request.session.request(method=methond,url=url,params=data,headers=header)
        elif methond.lower() == 'post':
            res=Request.session.request(method=methond,url=url,json=data,headers=header)
        
            # assert caseinfo['validate']['code'] == res.json()['code']
            # assert caseinfo['validate']['msg'] == res.json()['msg']