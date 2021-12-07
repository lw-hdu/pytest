'''
Descripttion: 
version: 
Author: Liuwen
Date: 2021-11-30 14:27:06
LastEditTime: 2021-11-30 14:36:05
'''
import requests
class Request:
    session = requests.session()
    def send_request(self,methond,url,data):
        if methond == 'get':
           res = Request.session.request(method=methond,url=url,params=data)
        elif methond == 'post':
           res = Request.session.request(method=methond,url=url,json=data)
        else:
            pass
        return res