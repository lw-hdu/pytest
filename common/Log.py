'''
Descripttion: 
version: 
Author: Liuwen
Date: 2021-12-06 13:17:43
LastEditTime: 2021-12-06 14:43:04
'''
import time
import logging

logging.basicConfig(level=logging.INFO)

def log(title,message):
    log = logging.getLogger(title)
    log.info(message)

log('test','this is info message')