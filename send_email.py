import smtplib
from config import Config
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(title, contain, file_name):
    mail_host = Config.mail_host
    mail_user = Config.mail_user
    mail_pass = Config.mail_pass
    sender = Config.sender
    receivers = Config.receivers

    # 设置email信息
    # 邮件内容设置
    message = MIMEMultipart()
    message.attach(MIMEText(contain, 'plain', 'utf-8'))
    # 邮件主题
    message['Subject'] = title
    # 发送方信息
    message['From'] = sender
    # # 接受方信息
    # message['To'] = receivers[0]

    # 邮件附件
    att = MIMEText(open(file_name, 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment;filename="%s"' % (file_name)
    message.attach(att)

    # 登录并发送邮件
    try:
        smtpObj = smtplib.SMTP()
        # 连接到服务器
        smtpObj.connect(mail_host, 25)
        # 登录到服务器
        smtpObj.login(mail_user, mail_pass)
        # 发送
        smtpObj.sendmail(
            sender, receivers, message.as_string())
        # 退出
        smtpObj.quit()
        print('success')
    except smtplib.SMTPException as e:
        print('error', e)  # 打印错误


if __name__ == "__main__":
    send_email("title", "message", "result.txt")