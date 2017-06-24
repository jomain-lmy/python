import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
# 第三方 SMTP 服务
# emailcontainer='dfghjklksldfjlksdjflsdjflsadjflsjd sdkfjlds kjlsadjfkls lksdajfl'
mail_host="smtp.qq.com"  #设置服务器
mail_user="1273046149@qq.com"    #用户名
mail_pass="ofkaypupwehvheib"   #口令 
 
 
sender = '1273046149@qq.com'
receivers = ['1075823894@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
message = MIMEText('emailcontainer', 'plain', 'utf-8')
message['From'] = Header("1273046149@qq.com", 'utf-8')
message['To'] =  Header("1075823894@qq.com", 'utf-8')
 
subject = 'new'
message['Subject'] = Header(subject, 'utf-8')

 
try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 587)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")

