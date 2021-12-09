'''
Descripttion: 
Author: Liuwen
Date: 2021-12-07 17:14:57
LastEditTime: 2021-12-08 11:01:16
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestUI(unittest.TestCase):
    def test_login(self):
        global driver
        # # 防止打印一些无用的日志
        # option = webdriver.ChromeOptions()
        # option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
        # driver = webdriver.Chrome(chrome_options=option)
        driver = webdriver.Chrome()
        driver.get('http://10.0.10.131/')
        driver.find_element(By.XPATH,'//input[@placeholder="请输入用户名"]').send_keys('admin')
        driver.find_element(By.XPATH,'//input[@placeholder="请输入密码"]').send_keys('1qaz!QAZ')
        driver.find_element(By.XPATH,'//span[text()=" 登  录 "]').click()

        
        # driver.find_element(By.XPATH,'//span[text()="电站管理"]').click()
        
       

if __name__ == '__main__':
    unittest.main()