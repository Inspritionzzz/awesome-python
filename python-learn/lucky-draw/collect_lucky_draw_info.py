from tqdm import tqdm
import requests

import os
import logging

from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib

'''
    1、获取更新动态
    2、提取中奖信息动态
    3、发送邮件
'''

logger = logging.getLogger(__name__)

def get_all_items():

    url = 'https://t.bilibili.com/?spm_id_from=444.41.0.0'

    pass

def send_email():



    pass

def send_simple_message():

    with open(".\\file\\textfile.txt") as fp:
        msg = EmailMessage()
        msg.set_content(fp.read())

    msg ['Subject'] = f'The contents of'
    msg['From'] = '591831416@qq.com'
    msg['To'] = '1011919111@qq.com'

    # 通过自己的 SMTP 发送信息
    s = smtplib.SMTP('localhost')
    s.sendmail(msg)
    s.quit()

    pass




if __name__ == '__main__':

    send_email()
    pass