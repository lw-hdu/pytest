'''
Descripttion: 
version: 
Author: Liuwen
Date: 2021-12-07 10:05:51
LastEditTime: 2021-12-07 11:34:49
'''

'''
通过Template给yaml文件中的字段传参
'''
import json
from string import Template
from common.Readyaml import get_yaml_file

file = get_yaml_file('common\\test.yaml')

temp = Template(json.dumps(file))
d={'name':'liuwen','passwd':'123456789'}
print(temp.safe_substitute(d))