'''
Descripttion: 
version: 
Author: Liuwen
Date: 2021-12-07 10:05:51
<<<<<<< HEAD
LastEditTime: 2021-12-14 14:55:12
=======
LastEditTime: 2021-12-08 11:08:58

'''

'''
通过Template给yaml文件中的字段传参
'''
import json
from string import Template
from common.Readyaml import get_yaml_file

file = get_yaml_file('demo_test\\test.yaml')
temp = Template(json.dumps(file))
d={'name':'liuwen','passwd':'123456789'}
print(temp.safe_substitute(d))
