import urllib
import urllib.request
import io  
import sys  
import re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
def email(str):
    import smtplib
    from email.mime.text import MIMEText
    from email.header import Header
    hia = str
    # 第三方 SMTP 服务
    mail_host="smtp.mxhichina.com"  #设置服务器
    mail_user="jomain@changewaver.com"    #用户名
    mail_pass="Lmy199864"   #口令 
   
   
    sender = 'jomain@changewaver.com'
    receivers = ['bayu@ahu114.me']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
    message = MIMEText(hia, 'plain', 'utf-8')
    message['From'] = Header("jomain@changewaver.com", 'utf-8')
    message['To'] =  Header("bayu@ahu114.me", 'utf-8')
 
    subject = '来新消息啦，快去看看'
    message['Subject'] = Header(subject, 'utf-8')
    
 
    try:
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print ("邮件发送成功")
    except smtplib.SMTPException:
        print ("Error: 无法发送邮件")
data = {}
url = "http://jwc.ahu.cn/main/index.asp"
data = urllib.request.urlopen(url).read()
data = data.decode('gb2312','ignore')
data1 = re.findall("<td>.*</table",data)
with open('1.txt', 'rt', encoding='gb2312') as f:
    old = f.readline()
f.close()

f=open("1.txt","w")
i = 0 
k = 1
for x in data1:
    if i:
        data2 = x
    i = 1
data3 = re.findall("title='.*?>",data2,re.M|re.I)
for y in data3:
    data4 = re.search("(title)='(.*?)'>",y,re.M|re.I)
    f.write(data4.group(2)+"\n")
    if i:
        new = data4.group(2)
        fuck = re.search(new,old)
        i=0
        if fuck:
            print("no")
        else:
            email(new)





f.close()