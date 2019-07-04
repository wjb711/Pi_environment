from flask import Flask, render_template, request
from my_json import readjson,writejson
import os
import sys
app = Flask(__name__)

@app.route('/')

def index():

    return render_template('test1.html')


@app.route('/login_ok')

def loginok():

    return render_template('login.html')



@app.route('/login', methods=['post'])



#@app.route('/')
def login():

    name = request.form.get('name')

    password = request.form.get('password')
    print(name,password)
    if name == 'pi' and password == 'gi-de123':

        return render_template('login.html')

        #return x
    else:
        return render_template('test1.html')
#        pass

@app.route('/DHCP')
def DHCP():
    #name=str(random.random())
    os.system('cp -f dhcp.conf /etc/dhcpcd.conf')
    print('hello, I_m here0')
    return  '''
<html>
<body>
<br>已提交，重启后生效</br>
<br><a href="../login_ok">Back</a></br>
</body>
</html>
'''




@app.route('/static_ip',methods=['GET','POST'])
def static_ip():
    #name=str(random.random())
    #os.system('export DISPLAY=:0 && xfreerdp -g 1024x768 -u wanju@accounts -p pr
    ip = request.form.get('ip')
    gateway = request.form.get('gateway')
    dns = request.form.get('dns')
    if ip and gateway and dns:
        print(ip,gateway,dns)

        with open('dhcpcd.conf','r') as f:
            x=f.readlines()
#for x0 in x:
#    print(x0)
        line1='interface eth0'
        line2='static ip_address='+ip
        line3='static routers='+gateway
        line4='static domain_name_servers='+dns
        x.append(line1+'\n')
        x.append(line2+'\n')
        x.append(line3+'\n')
        x.append(line4+'\n')
        for x0 in x:
            print(x0)

        with open('/etc/dhcpcd.conf','w') as f:
            for x0 in x:
                f.write(x0)




        return '''
<html>
<body>
<br>已提交，重启后生效</br>
<br><a href="../login_ok">Back</a></br>
</body>
</html>

'''
#        print('hello, I_m here0')
    else:
        return  '''
<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8">
<title>from_test</title></head>
<body><form method="post" action="static_ip">    IP：<input type="text" name="ip"/>  gateway：<input type="text" name="gateway"/> DNS：<input type="text" name="dns"/>  <input type="submit" value="Submit"/></form>
<br>重启后生效</br>
<br><a href="../login_ok">Back</a></br>
</body>
</html>

'''


@app.route('/tem_max',methods=['GET','POST'])
def tem_max():
    #name=str(random.random())
    name = request.form.get('name')
    if name:
        writejson('config.json','tem_max',name)
    else:
        print('it is none')
    print('hello, I_m here0')
    print('look:',name,type(name))
    tem_max=readjson('config.json','tem_max')
    print(tem_max)
    template='''
<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8">
<title>from_test</title></head>
<body><form method="post" action="tem_max">    温度报警值（摄氏度）输入例如 30，35，40：<input type="text" name="name"/>     <input type="submit" value="Submit"/></form>
<br><a href="../login_ok">Back</a></br>
</body>
</html>

'''
    return '当前值设定为：'+str(tem_max)+template

@app.route('/hum_max',methods=['GET','POST'])
def hum_max():

    name = request.form.get('name')
    if name:
        writejson('config.json','hum_max',name)
    else:
        print('it is none')
    print('hello, I_m here0')
    print('look:',name,type(name))
    hum_max=readjson('config.json','hum_max')
    print(hum_max)
    template='''
<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8">
<title>from_test</title></head>
<body><form method="post" action="hum_max">    湿度报警值（百分比）输入例如 70，80，90：<input type="text" name="name"/>     <input type="submit" value="Submit"/></form>
<br><a href="../">Back</a></br>
</body>
</html>

'''
    return '当前值设定为：'+str(hum_max)+template


@app.route('/ntp_server',methods=['GET','POST'])
def ntp_server():

    name = request.form.get('name')
    if name:
        writejson('config.json','ntp_server',name)
    else:
        print('it is none')
    print('hello, I_m here0')
    print('look:',name,type(name))
    ntp_server=readjson('config.json','ntp_server')
    print(ntp_server)
    template='''
<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8">
<title>from_test</title></head>
<body><form method="post" action="ntp_server">    NTP server 例如 10.102.10.1：<input type="text" name="name"/>     <input type="submit" value="Submit"/></form>
<br><a href="../login_ok">Back</a></br>
</body>
</html>

'''
    return '当前值设定为：'+str(ntp_server)+template



@app.route('/sender',methods=['GET','POST'])
def sender():
    def_name=sys._getframe().f_code.co_name

    name = request.form.get('name')
    if name:
        writejson('config.json',str(def_name),name)
    else:
        print('it is none')
    print('hello, I_m here0')
    print('look:',name,type(name))
    def_name=readjson('config.json',str(def_name))
    #print(sender)
    template='''
<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8">
<title>from_test</title></head>
<body><form method="post" action=sender>     例如 jianbo.wang@gi-de.com：<input type="text" name="name"/>     <input type="submit" value="Submit"/></form>
<br><a href="../login_ok">Back</a></br>
</body>
</html>

'''
    return '当前值设定为：'+str(def_name)+template


@app.route('/receivers',methods=['GET','POST'])
def receivers():
    def_name=sys._getframe().f_code.co_name

    name = request.form.get('name')
    if name:
        writejson('config.json',str(def_name),name)
    else:
        print('it is none')
    print('hello, I_m here0')
    print('look:',name,type(name))
    def_name=readjson('config.json',str(def_name))
    #print(sender)
    template='''
<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8">
<title>from_test</title></head>
<body><form method="post" action=receivers>     例如 jianbo.wang@gi-de.com,10054053@qq.com：<input type="text" name="name"/>     <input type="submit" value="Submit"/></form>
<br><a href="../login_ok">Back</a></br>
</body>
</html>

'''
    return '当前值设定为：'+str(def_name)+template


@app.route('/mail_server',methods=['GET','POST'])
def mail_server():
    def_name=sys._getframe().f_code.co_name

    name = request.form.get('name')
    if name:
        writejson('config.json',str(def_name),name)
    else:
        print('it is none')
    print('hello, I_m here0')
    print('look:',name,type(name))
    def_name=readjson('config.json',str(def_name))
    #print(sender)
    template='''
<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8">
<title>from_test</title></head>
<body><form method="post" action=mail_server>     例如 10.4.172.3 ：<input type="text" name="name"/>     <input type="submit" value="Submit"/></form>
<br><a href="../login_ok">Back</a></br>
</body>
</html>

'''
    return '当前值设定为：'+str(def_name)+template


@app.route('/subject',methods=['GET','POST'])
def subject():
    def_name=sys._getframe().f_code.co_name

    name = request.form.get('name')
    if name:
        writejson('config.json',str(def_name),name)
    else:
        print('it is none')
    print('hello, I_m here0')
    print('look:',name,type(name))
    try:
        def_name=readjson('config.json',str(def_name))
    except:
        def_name=''
    #print(sender)
    template='''
<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8">
<title>from_test</title></head>
<body><form method="post" action=subject>     例如 某地机房温湿度检测报警 ：<input type="text" name="name"/>     <input type="submit" value="Submit"/></form>
<br><a href="../login_ok">Back</a></br>
</body>
</html>

'''
    return '当前值设定为：'+str(def_name)+template


@app.route('/content',methods=['GET','POST'])
def content():
    def_name=sys._getframe().f_code.co_name

    name = request.form.get('name')
    if name:
        writejson('config.json',str(def_name),name)
    else:
        print('it is none')
    print('hello, I_m here0')
    print('look:',name,type(name))
    try:
        def_name=readjson('config.json',str(def_name))
    except:
        def_name=''
    #print(sender)
    template='''
<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8">
<title>from_test</title></head>
<body><form method="post" action=content>     例如 某地机房温湿度检测报警 ：<input type="text" name="name"/>     <input type="submit" value="Submit"/></form>
<br><a href="../login_ok">Back</a></br>
</body>
</html>

'''
    return '当前值设定为：'+str(def_name)+template

@app.route('/reboot',methods=['GET','POST'])

def reboot():
    os.system('sudo reboot')



if __name__ == '__main__':


    app.run('0.0.0.0',debug=True)
