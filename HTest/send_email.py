#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 发送邮件
import os
from .logger import logger
from HTest import setting, new_report
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
from email.header import Header


def send_email(file):
    # 邮件配置
    username_send = '1285642171@qq.com'  # 发件人
    username_received = ['l.tao@hang-shu.com']  # 收件人多人
    email_server = 'smtp.qq.com'  # 邮箱服务端url
    username_code = 'bancxgdgvdevbafd'  # 邮箱授权码

    """
    # 邮件发送
    content = "这是一份邮件"
    email = MIMEText(content, 'plain', 'utf-8')  # 文本形式的邮件
    email['Subject'] = '邮件主题'
    email['From'] = username_send
    email['To'] = ','.join(username_received)
    # 图片文件附件
    att1 = MIMEBase('application', 'octet-stream')
    att1.set_payload(open("123.jpeg", 'rb').read())
    att1.add_header('Content-Disposition', 'attachment', filename=Header('123.jpeg', 'gbk').encode())
    encoders.encode_base64(att1)
    email.attach(att1)
    """


    # 构造MIMEMultipart对象做为根容器
    email = MIMEMultipart()
    # 设置根容器属性
    email['Subject'] = '自动化测试报告'
    email['From'] = username_send
    email['To'] = ','.join(username_received)

    # 构造MIMEText对象做为邮件显示内容并附加到根容器
    text_msg = MIMEText("Hi All,\n \n   这是本次测试的测试报告，详情见附件。\n \nBest Wishes!")
    email.attach(text_msg)
    # 构造MIMEBase对象做为邮件附件内容并附加到根容器
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(open(file, 'rb').read())
    att.add_header('Content-Disposition', 'attachment', filename=Header(file, 'gbk').encode())
    encoders.encode_base64(att)
    email.attach(att)

    # 发邮件
    smtp = smtplib.SMTP_SSL(email_server, port=465)
    smtp.login(username_send, username_code)
    smtp.sendmail(username_send, ','.join(username_received), email.as_string())
    smtp.quit()
    logger.info("测试报告已发送成功")


if __name__ == '__main__':
    attr = os.path.join(setting.TEST_REPORT)
    report = new_report(attr)
    send_email(report)
