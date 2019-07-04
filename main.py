import Adafruit_DHT
from i2c import display_led as display
import datetime
import json
import subprocess
import time
import os
import RPi.GPIO as GPIO
from admin.my_json import readjson, writejson

def external_email():
#外部邮件的发送方法
    import smtplib
    from email.header import Header
    from email.mime.text import MIMEText
    mail_host = "smtp.163.com"      # SMTP服务器
    mail_user = "18970078166"                  # 用户名
    mail_pass = "wjb711"               # 授权密码，非登录密码

    sender = '18970078166@163.com'    # 发件人邮箱(最好写全, 不然会失败)
    #receivers = ['18970078166@163.com','10054053@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    #title = '功能性测试'
    #global content
    #print ('content is:',content,type(content))
    #content="this is for test"
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


def internal_email():
#内部邮件的发送方法
    import smtplib
    #from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    #print ('hello')

    smtp = smtplib.SMTP()
    smtp.connect(mail_server)
    #smtp.login(username, password)
    #msg = MIMEMultipart('mixed')
    #global content
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = title
    smtp.sendmail(sender, receivers, msg.as_string())
    smtp.quit()
    #print ('ok',email_address,'ok1')








def ip():
#ip获取方法
    cmd = "hostname -I | cut -d\' \' -f1"
    IP = str(subprocess.check_output(cmd, shell = True )).split('\'')[1].split('\\')[0]
    return IP

def writejson():
#记录历史，写json文件的方法
    try:
        with open('/var/www/html/rpi-TempRuntime/web/data/min/'+date+".json","r") as f:
            load_dict = json.load(f)
    except:
        load_dict=[]


    dict0={}
    dict0['tmp']=str(tmp)
    dict0['hmt']=str(hmt)
    dict0['time']=str(time0)
    load_dict.append(dict0)
    with open('/var/www/html/rpi-TempRuntime/web/data/min/'+date+".json","w") as f:

        json.dump(load_dict,f)

def beep():
#    import time
#    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(15,GPIO.OUT)
    GPIO.output(15,GPIO.HIGH)
    time.sleep(2)
    GPIO.output(15,GPIO.LOW)

if __name__=='__main__':
#主函数
    sensor = Adafruit_DHT.DHT22
    #传感器设置为DHT22, 驱动选用Adafruit_DHT

    tem_MAX=int(readjson('./admin/config.json','tem_max'))
    hum_MAX=int(readjson('./admin/config.json','hum_max'))
    #设定温度湿度最大值
    #receivers=readjson('./admin/config.json','receivers')
    #报警接收人

    ntp_server=readjson('./admin/config.json','ntp_server')

    #设定时钟服务器
    mail_server=readjson('./admin/config.json','mail_server')
    sender=readjson('./admin/config.json','sender')
    receivers=readjson('./admin/config.json','receivers')
    subject=readjson('./admin/config.json','subject')
    content=readjson('./admin/config.json','content')
    print(receivers,type(receivers))
    receivers=receivers.split(',')
    print(receivers,type(receivers))
    if int(time.time()/60)%10==0:
        os.system('sudo ntpdate '+ntp_server)
        print('sudo ntpdate '+ntp_server)
    #每十分钟同步一次时钟

    humidity, temperature = Adafruit_DHT.read_retry(sensor, 27)
    print(humidity, temperature)
    #湿度和温度来自pin角27
    tmp="{:.1f}".format(temperature)
    hmt="{:.1f}".format(humidity)
    #格式化温湿度数值，保留一位小数
    if humidity <101:
    #如果湿度超过99， 传感器有些问题，经常湿度会到3000+，引起不必要的麻烦，故这里使用软件方式跳过这些非正常值



        date = datetime.datetime.now().strftime("%Y-%m-%d")

        time0 = datetime.datetime.now().strftime("%H:%M")
        print(tmp,hmt,date,time0,ip())

        display("Temperature:"+tmp+"C","Humidity:"+hmt+"%",time0,ip())
        #led显示器上显示温度，湿度
        writejson()
        #把每分钟的数据，写入json， 以方便网页上显示
        if temperature >tem_MAX or humidity >hum_MAX:
            beep()
            #print(tem)
            print(subject,type(subject))
            title=str(subject)+str(tmp)+'*C'+'湿度:'+str(hmt)+'%'
            print(content,type(content))
            #content='hello,world'
            #title=str(subject)
            #邮件标题
            #global content
            #
            #邮件正文

            if ip().startswith('10.102'):

                internal_email()
            else:
                external_email()



    else:
        pass
