#树莓派温湿度环境工作站，传感器选DHT22,显示屏选LCD2004_IIC
import Adafruit_DHT
from i2c import display_led as display
import datetime
import json
import subprocess
import time
import os

def external_email():
#外部邮件的发送方法
    import smtplib
    from email.header import Header
    from email.mime.text import MIMEText
    mail_host = "smtp.163.com"      # SMTP服务器
    mail_user = "xxxx"                  # 用户名
    mail_pass = "xxxx"               # 授权密码，非登录密码

    sender = 'xxxx@163.com'    # 发件人邮箱(最好写全, 不然会失败)
    #receivers = ['xxxx@163.com','xxxx@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

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
    smtp.connect('x.x.x.x')
    #smtp.login(username, password)
    #msg = MIMEMultipart('mixed')
    #global content
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = title
    smtp.sendmail('EnvMonitor.DCC@gi-de.com', receivers, msg.as_string())
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
    dict0['time']=str(time)
    load_dict.append(dict0)
    with open('/var/www/html/rpi-TempRuntime/web/data/min/'+date+".json","w") as f:

        json.dump(load_dict,f)
if __name__=='__main__':
#主函数
    sensor = Adafruit_DHT.DHT22
    #传感器设置为DHT22, 驱动选用Adafruit_DHT

    tem_MAX=31
    hum_MAX=9    #设定温度湿度最大值
    receivers=['xxxxg@gi-de.com','xxxx3@qq.com','xxxx6@163.com']
    #报警接收人
        
    ntp_server='x.x.x.x'
    #设定时钟服务器
    if int(time.time()/60)%10==0:
        os.system('sudo ntpdate '+ntp_server)
        print('sudo ntpdate '+ntp_server)
    #每十分钟同步一次时钟
   
    humidity, temperature = Adafruit_DHT.read_retry(sensor, 27)
    #湿度和温度来自pin角27
    tmp="{:.1f}".format(temperature)
    hmt="{:.1f}".format(humidity)
    #格式化温湿度数值，保留一位小数
    if humidity <99:
    #如果湿度超过99， 传感器有些问题，经常湿度会到3000+，引起不必要的麻烦，故这里使用软件方式跳过这些非正常值
    
        

        date = datetime.datetime.now().strftime("%Y-%m-%d")

        time=now = datetime.datetime.now().strftime("%H:%M")
        print(tmp,hmt,date,time,ip())

        display("Temperature:"+tmp+"C","Humidity:"+hmt+"%",time,ip())
        #led显示器上显示温度，湿度
        writejson()
        #把每分钟的数据，写入json， 以方便网页上显示
        if temperature >tem_MAX or humidity >hum_MAX:
            #print(tem)

            title='HSDN Server room 温度:'+str(tmp)+'*C'+'湿度:'+str(hmt)+'%'
            #邮件标题
            #global content
            content='高安机房温湿度报警，请尽快处理'
            #邮件正文

            if ip().startswith('内网地址'):
                
                internal_email()
            else:
                external_email()
        
        
        
    else:
        pass
