'''
Descripttion: 接口信息写入yaml文件，读取yaml文件内容
version: 
Author: Liuwen
Date: 2021-11-24 16:12:24
LastEditTime: 2022-03-02 09:35:04
'''
import yaml
import os

def get_file_path():
    #获取当前路径的上一级
    filepath=os.path.abspath(__file__).split('common')[0]
    return filepath


def get_yaml_file(filename):
    with open(get_file_path()+filename,'r',encoding='utf-8') as f:
        value=yaml.load(stream=f,Loader=yaml.FullLoader)
        return value

#print(get_yaml_file('demo_test\\command\\find_commandpage.yaml'))