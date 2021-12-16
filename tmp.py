'''
Descripttion: 
version: 
Author: Liuwen
Date: 2021-12-07 10:05:51
LastEditTime: 2021-12-15 16:27:39
=======
LastEditTime: 2021-12-08 11:08:58

'''

'''
通过Template给yaml文件中的字段传参
'''
# import json
# from string import Template
# from common.Readyaml import get_yaml_file

# file = get_yaml_file('demo_test\\test.yaml')
# temp = Template(json.dumps(file))
# d={'name':'liuwen','passwd':'123456789'}
# print(temp.safe_substitute(d))





import smtplib
import time
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication 
from email.header import Header
 
if __name__ == '__main__':
        currentTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        fromaddr = 'lw_hdu@163.com'
        password = 'ZXFOMKFKOXDDTGYJ'
        toaddrs = ['liuwen10@longi.com']
 
        content = f'你好，现在是{currentTime}，\n自动化测试已完成，详细信息参考附件日志'
        textApart = MIMEText(content,'plain','utf-8')
 
        # imageFile = '1.png'
        # imageApart = MIMEImage(open(imageFile, 'rb').read(), imageFile.split('.')[-1])
        # imageApart.add_header('Content-Disposition', 'attachment', filename=imageFile)
 
        # pdfFile = '算法设计与分析基础第3版PDF.pdf'
        # pdfApart = MIMEApplication(open(pdfFile, 'rb').read())
        # pdfApart.add_header('Content-Disposition', 'attachment', filename=pdfFile)
    
 
        # zipFile = '算法设计与分析基础第3版PDF.zip'
        # zipApart = MIMEApplication(open(zipFile, 'rb').read())
        # zipApart.add_header('Content-Disposition', 'attachment', filename=zipFile)

        logFile = r'F:\pytestdemo\test.log'
        logApart = MIMEApplication(open(logFile,'rb').read())
        logApart.add_header('Content-Disposition', 'attachment', filename=logFile)
 
        m = MIMEMultipart()
        m.attach(textApart)
        # m.attach(imageApart)
        # m.attach(pdfApart)
        # m.attach(zipApart)
        m.attach(logApart)

        m['From'] = Header(fromaddr)
        m['To'] = Header(toaddrs[0])
        m['Subject'] = Header('测试结果通知邮件')


 
        try:
            server = smtplib.SMTP('smtp.163.com')
            server.login(fromaddr,password)
            server.sendmail(fromaddr, toaddrs, m.as_string())
            print('邮件发送成功')
            server.quit()
        except smtplib.SMTPException as e:
            print('error:',e) #打印错误