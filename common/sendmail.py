# coding:utf-8
import os
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from util.log import log
from common.read_data import r

base_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
reportpath=os.path.join(base_path,'page','report')
# 163的用户名和授权密码
send_name =r.get_email('name')
send_pwd = r.get_email('pwd')
receive = r.get_email('addr')
subject=r.get_email('subject')
text=r.get_email('email_text')

def sendmail():
    #获取报告目录下最新的测试报告
    dirs = os.listdir(reportpath)
    for dir in dirs:
        if dir == 'index.html':
            newreportname = dir
            log.info('The new report name: {}'.format(newreportname))
            # 创建一个带附件的邮件实例
            message=MIMEMultipart()
            # 邮件的其他属性
            message['From'] = send_name   #发送人
            message['Subject'] = Header(subject, 'utf8').encode()
            message['To'] = receive   #接收人
            # 邮件正文内容
            attr2 = MIMEText(text, 'plain', 'utf-8')
            message.attach(attr2)
            #构造附件
            path=os.path.join(reportpath,newreportname)
            attr1=MIMEText(open(path,'rb').read(),'base64','utf-8')
            attr1["content_Type"]='application/octet-stream'
            attr1["Content-Disposition"] = 'attachment; filename="index.html"'
            message.attach(attr1)
            try:
                server = smtplib.SMTP('smtp.163.com', 25)
                server.login(send_name, send_pwd)
                server.sendmail(send_name, receive,message.as_string())
                log.info("发送邮件至 {}".format(receive))
                log.info("发送邮件成功")
            except Exception as e:
                log.error('失败：' + str(e))
            break
    else:
        log.debug("未找到html测试报告")


if __name__ == '__main__':
    sendmail()