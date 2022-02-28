'''
Descripttion: 
Author: Liuwen
Date: 2021-12-20 13:59:25
LastEditTime: 2021-12-27 09:43:47
'''

import pymysql

def sel_db(sql):
    #连接mysql数据库
    conn = pymysql.connect(host='10.0.10.130', user='root', password='123456', db='monitor_1', port=3306,charset="utf8")
    #创建一个游标对象 cursor,（游标指mysql里的光标对象_）
    cursor = conn.cursor()
    #执行sql语句
    cursor.execute(sql)
    #查询所有记录
    results = cursor.fetchall()
    #关闭数据库连接
    conn.close()
    cursor.close()

    return results

# print(sel_db("SELECT * FROM  mon_conf_command WHERE command_name ='11111'"))