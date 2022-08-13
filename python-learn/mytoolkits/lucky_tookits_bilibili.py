"""
    bili自动参与抽奖工具
"""
import datetime
import logging
import smtplib
from email.mime.text import MIMEText
import MySQLdb


def send_mail(to_list, sub, content):
    #设置服务器，用户名、口令以及邮箱的后缀
    mail_host = "591831416@qq.com"
    mail_user = "xiepan1990929"
    mail_pass = "3330372"
    mail_postfix = "126.com"
    me = mail_user+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content)
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = to_list
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user, mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception:
        print('邮件发送错误...')
        return False
    finally:
        return True

if __name__ == '__main__':

    FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
    logging.basicConfig(format=FORMAT)
    d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
    logger = logging.getLogger('tcpserver')
    logger.warning('Protocol problem: %s', 'connection reset', extra=d)

    print("抽奖程序启动成功...%s".format(datetime.datetime))

