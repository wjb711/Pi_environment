#start_ip.py baiti neirong 18970078166@163.com 10054053@qq.com
import sys
import time
def internal_email():
    import smtplib
    #from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    #print ('hello')

    smtp = smtplib.SMTP()
    smtp.connect('10.4.172.3')
    #smtp.login(username, password)
    #msg = MIMEMultipart('mixed')
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = title
    smtp.sendmail('jianbo.wang@gi-de.com', receivers, msg.as_string())
    smtp.quit()
    #print ('ok',email_address,'ok1')

def get_host_ip():
    import socket
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('8.8.8.10', 890))
        except:
            pass
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip

def sendEmail():
    import smtplib
    from email.header import Header
    from email.mime.text import MIMEText
    mail_host = "smtp.163.com"      # SMTP服务器
    mail_user = "18970078166"                  # 用户名
    mail_pass = "wjb711"               # 授权密码，非登录密码

    sender = '18970078166@163.com'    # 发件人邮箱(最好写全, 不然会失败)
    #receivers = ['18970078166@163.com','10054053@qq.com']  # 接收邮件，可设置为                                                                                                                     你的QQ邮箱或者其他邮箱

    #title = '功能性测试'
    #global content
    #print ('content is:',content,type(content))
    #content="this is for test"
    #content='今日基金行情'+'\n'+'今日基金行情'+'\n'
    message = MIMEText(content, 'plain',"utf-8")  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)
time.sleep(20)
title=get_host_ip()
content='来自树莓派环境监测系统的问候'
receivers=sys.argv[3:]

if title.startswith('0'):
    pass
elif title.startswith('10.102'):
    internal_email()
else:
    print(title, type(title))
    sendEmail()
#content='来自树莓派环境监测系统的问候'
#receivers=sys.argv[3:]
#sendEmail()
#internal_email()
