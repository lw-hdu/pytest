'''
Descripttion: 
Author: Liuwen
Date: 2021-12-16 11:50:38
LastEditTime: 2021-12-16 14:04:39

shutil.make_archive(base_name, format, root_dir, base_dir)
base_name，是加上完整路径（不能缩写）的文件或文件夹名
format一般是zip，其它tar之类也行
root_dir是要压缩的目录或文件
base_dir是压缩包里的文件层级。如你写a/b/c，这样所有文件都会塞到最底层的c文件夹中。

把F:\pytestdemo\\reports文件压缩，在F:\pytestdemo下生成allure-report.zip
'''
import shutil

shutil.make_archive(r'F:\pytestdemo\allure-report','zip','reports',r'F:\pytestdemo\reports')