import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import time

class smtp:
    def __init__(self):
        self.sendHost = 'smtp.qq.com'
        self.sendUser = '11241066@qq.com'
        self.sendPass = 'ltnexnjuzfykcakk'
        self.sendNick = '发件人'
        self.receUser = 'city@nanzc.com'
        self.receNick = '收件人'

    @staticmethod
    def getNowtime():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def sendMail(self):

        result = True

        try:
            msg = MIMEText(self.getNowtime(), 'plain', 'utf-8')
            msg['From'] = formataddr([self.sendNick, self.sendUser])
            msg['To'] = formataddr([self.receNick, self.receUser])
            msg['Subject'] = "测试邮件"
            server = smtplib.SMTP_SSL(self.sendHost, 465)  # ，端口是25
            server.login(self.sendUser, self.sendPass)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(self.sendUser, [self.receUser, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件

            server.quit()  # 关闭连接
        except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            result = False

        return result