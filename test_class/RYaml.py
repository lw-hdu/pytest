'''
Descripttion: 接口信息写入yaml文件，读取yaml文件内容
version: 
Author: Liuwen
Date: 2021-11-24 16:12:24
LastEditTime: 2021-12-20 10:50:41
'''
import yaml
import os

# def get_file_path():
#     #获取当前路径的上一级
#     filepath=os.path.abspath(__file__).split('common')[0]
#     return filepath


def get_yaml_file(file):
    with open(file,'r',encoding='utf-8') as f:
        value=yaml.load(stream=f,Loader=yaml.FullLoader)
        return value

# print(get_yaml_file('F:\\pytestdemo\\demo_test\\power\\find_allpower.yaml'))