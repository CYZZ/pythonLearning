
from email.mime.text import MIMEText
msg = MIMEText('hello, send by Python...from chiyuze第二份邮件','plain','utf-8')


#填写完整，要不然会被判断为垃圾邮件
msg['From'] = 'cyz19910420@163.com'
msg['To'] = '806985831@qq.com'
msg['Subject'] = '来自Python的邮件'

#输入Email地址和口令
# from_addr = input('From:')
# password = input('Password:')
# to_addr = input('To:')
#
# #输入SMTP服务器地址：
# smtp_server = input('SMTP server:')
from_addr = 'cyz19910420@163.com'
password = ''
to_addr = '806985831@qq.com'
smtp_server = 'smtp.163.com'

import smtplib
server = smtplib.SMTP(smtp_server, 25) #SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr, [to_addr],msg.as_string())
server.quit()