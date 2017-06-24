import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
# 第三方 SMTP 服务
mail_host="smtp.mxhichina.com"  #设置服务器
mail_user="jomain@changewaver.com"    #用户名
mail_pass="Lmy199864"   #口令 
 
 
sender = 'jomain@changewaver.com'
receivers = ['lmyundo@gmail.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
message = MIMEText('you are goning to die', 'plain', 'utf-8')
message['From'] = Header("jomain@changewaver.com", 'utf-8')
message['To'] =  Header("lmyundo@gmail.com", 'utf-8')
 
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')
    
 

smtpObj = smtplib.SMTP() 
smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
smtpObj.login(mail_user,mail_pass)
smtpObj.sendmail(sender, receivers, message.as_string())

print ("邮件发送成功")

# print ("Error: 无法发送邮件")