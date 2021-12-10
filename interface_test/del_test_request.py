'''
Descripttion: 
version: 
Author: Liuwen
Date: 2021-12-01 15:01:13
LastEditTime: 2021-12-10 10:18:21
'''
from os import listdir
from typing_extensions import Self 
from _pytest.mark import param
import pytest
from common.Request import Request
from common.Readyaml import get_yaml_file


class TestRequest:
    file_path = ''

    def __init__(self,path) -> None:
        self.file_path = path

    @pytest.mark.parametrize('caseinfo',get_yaml_file(file_path))
    def test_device(self,caseinfo,get_token):
        name=caseinfo['name']
        header={'Authorization':get_token}
        methond=caseinfo['request']['methond']
        url=caseinfo['request']['url']
        data=caseinfo['request']['data']
        if methond.lower() == 'get':
            res=Request.session.request(method=methond,url=url,params=data,headers=header)
        elif methond.lower() == 'post':
            res=Request.session.request(method=methond,url=url,json=data,headers=header)
        
            assert caseinfo['validate']['code'] == res.json()['code']
            assert caseinfo['validate']['msg'] == res.json()['msg']