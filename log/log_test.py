'''
Descripttion: 
Author: Liuwen
Date: 2022-02-23 15:23:20
LastEditTime: 2022-02-23 16:43:57
'''
import logging
import os
import datetime

log = logging.getLogger()
log.setLevel(logging.INFO)
#控制台输出日志
# consle = logging.StreamHandler()
# log.addHandler(consle)
#日志文件
base_dir = os.path.dirname(os.path.abspath(__file__))  #f:\pytestdemo\log
log_dir = os.path.join(base_dir,'logs') #f:\pytestdemo\log\logs
log_file = datetime.datetime.now().strftime('%Y-%m-%d')+'.log'  #2022-02-23.log
log_name = log_dir+'/'+log_file

#文件输出日志
file = logging.FileHandler(log_name,encoding='utf-8')
formatter = logging.Formatter('%(asctime)s %(filename)s->%(funcName)s %(lineno)d：%(levelname)s-->%(message)s ')
file.setFormatter(formatter)
log.addHandler(file)


log.info('日志输出测试')
# consle.close()
# log.removeHandler(consle)
file.close()
log.removeHandler(file)