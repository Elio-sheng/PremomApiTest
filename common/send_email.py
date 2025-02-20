"""
-*- coding: utf-8 -*-
"""
import os
import smtplib
import zipfile
from email.mime.text import MIMEText  # 正文用
from email.header import Header  # 标题用
from email.utils import formataddr


class SendEmail:

    def __init__(self, fujian_name, dirpath, outFullName):
        self.fujian_name = fujian_name
        self.dirpath = dirpath
        self.outFullName = outFullName

    def run(self):

        send_User = "1511098763@qq.com"  # 邮箱地址
        send_Password = "rnvxxuzyzwlhigdb"  # 163邮箱的smtp密码
        send_Smtp = "smtp.qq.com"  # 使用的邮箱smtp官方地址
        addreSsee = [
            "1511098763@qq.com", "18278571683@163.com",
            "Enzo.Liu@easyhealthcarecorp.com",
            "cindy.zhang@easyhealthcarecorp.com"
        ]  # 收件箱地址
        # 发送的附件内容
        # msg = MIMEText('hh', 'base64', 'utf-8')  # 数据编码方式是utf-8
        msg = MIMEText(open(self.fujian_name, 'rb').read(), "base64", "utf-8")
        msg['Content-Type'] = 'application/octet-stream'
        msg["Content-Disposition"] = 'attachment; filename=' + self.fujian_name

        # 第一种发件人方式：
        msg['From'] = send_User  # 发件人，声明收到邮件的时候发件人显示用（11不能写中文）
        # print(type(msg['From']))  # 是一个email的对象
        # u一般用在中文字符串前面，防止因为源码储存格式问题
        msg['Subject'] = Header(u'测试邮件', 'utf-8').encode()
        msg['To'] = u'test'  # 收件人的名字（随便取）

        # print(msg)  # 打印发送给接受的数据
        # print(type(msg))
        # 实例化一个邮箱
        smtp = smtplib.SMTP()
        smtp.connect(send_Smtp, 25)  # 这是发送出去的邮箱的smtp的地址和默认端口
        smtp.login(send_User, send_Password)  # 这是登录的账号和smtp密码，用于除了网页以外的客户端登录
        # 发送邮件，传入发送账号，接收账号，将from和to subject当做字符串传入
        smtp.sendmail(send_User, addreSsee, msg.as_string())
        smtp.quit()  # 关闭连接

    def zipDir(self):
        zip = zipfile.ZipFile(self.outFullName, "w", zipfile.ZIP_DEFLATED)
        for path, dirnames, filenames in os.walk(self.dirpath):
            # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
            fpath = path.replace(self.dirpath, '')

            for filename in filenames:
                zip.write(os.path.join(path, filename),
                          os.path.join(fpath, filename))
        zip.close()
        print('压缩成功')


# 调试是否调通
# a = SendEmail(r"send_dir.zip",r'send_dir',r"send_dir.zip")
# a.run()
# a.zipDir()
