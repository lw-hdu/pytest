'''
Descripttion: 
version: 
Author: Liuwen
Date: 2021-11-24 10:16:23
LastEditTime: 2021-12-16 11:19:21
'''
import os
import pytest
import time
# from common.SendEmail import SendEmail
from common.mail import SendEmail

if __name__ == '__main__':
    pytest.main()
    time.sleep(2)
    #使用allure生成测试报告
    # allure测试报告不能直接打开本地的html文件，要使用  allure open F:\pytestdemo\reports\ 渲染打开
    os.system("F:\\allure-2.9.0\\bin\\allure generate ./temps -o ./reports --clean")
    # os.system("allure open F:\\pytestdemo\\reports ")
    # os.system('Ctrl+C')
    # SendEmail()
    sendemail = SendEmail()
    sendemail.file_mail()