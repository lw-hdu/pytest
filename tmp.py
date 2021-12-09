'''
Descripttion: 
version: 
Author: Liuwen
Date: 2021-12-07 10:05:51
LastEditTime: 2021-12-08 10:34:37
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