import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(title, contain, file_name):
    # 设置服务器所需信息
    # 163邮箱服务器地址
    mail_host = 'smtp.163.com'
    # 163用户名
    mail_user = '1*********3'
    # 密码(部分邮箱为授权码)
    mail_pass = 'B*********G'
    # 邮件发送方邮箱地址
    sender = '13*********3@163.com'
    # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
    receivers = ["m******2@163.com", "2******9@qq.com"]

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