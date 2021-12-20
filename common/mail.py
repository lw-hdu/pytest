'''
Descripttion: 
Author: Liuwen
Date: 2021-12-16 10:15:55
LastEditTime: 2021-12-17 16:44:17
'''
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication 
from email.header import Header

class SendEmail:
    def __init__(self) -> None:
        self.from_addr = 'bipv001@longi.com'
        self.password = 'Longi@123'
        self.to_addr = ['liuwen10@longi.com']
        self.stmp_server = 'mail.longi.com'
        self.curtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        self.subject = '接口自动化测试结果通知'

    def send(self,message):
        #邮件头设置
        message['From'] = Header(self.from_addr)
        message['To'] = Header(self.to_addr[0])
        message['Subject'] = Header(self.subject)
        
        #开启发信服务
        server=smtplib.SMTP()
        server.connect(self.stmp_server,25)
        # server = smtplib.SMTP_SSL(self.stmp_server,465)
        
        try:
            #登录邮箱
            server.login(self.from_addr,self.password)
            #发送邮件
            server.sendmail(self.from_addr,self.to_addr,message.as_string())
            print('邮件发送成功')
            #关闭服务器
            server.quit()
            
        except smtplib.SMTPException as e:
            print('error:',e)

    def text_mail(self):
        #设置发送内容
        text = f'您好，今天是{self.curtime}'
        msg = MIMEText(text,'plain','utf-8')
        #调用发送方法
        self.send(msg)

        
    def file_mail(self):
        #设置发送内容
        content = f'您好，现在是{self.curtime}，\n接口自动化测试已完成，日志信息见附件'
        textApart = MIMEText(content,'plain','utf-8')
        #日志文件附件
        logFile = r'F:\pytestdemo\test.log'
        logApart = MIMEApplication(open(logFile,'rb').read())
        logApart.add_header('Content-Disposition', 'attachment', filename=logFile)
        #压缩文件附件
        zipFile = r'F:\pytestdemo\allure-report.zip'
        zipApart = MIMEApplication(open(zipFile, 'rb').read())
        zipApart.add_header('Content-Disposition', 'attachment', filename=zipFile)

        m = MIMEMultipart()
        m.attach(textApart)
        m.attach(logApart)
        m.attach(zipApart)

        #调用发送方法
        self.send(m)


# sendemail = SendEmail()
# sendemail.file_mail()