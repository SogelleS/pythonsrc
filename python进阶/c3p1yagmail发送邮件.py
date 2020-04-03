"""
需要连接邮箱服务器
15954458650@163.com     发件人邮箱
TOpenMail2048           授权码
smtp.163.com            163邮箱服务器

使用Yagmail 创建类对象
发送邮件(指定收件人，主题，内容)

"""

import yagmail

mail_ob = yagmail.SMTP(user='15954458650@163.com',\
                       password='TOpenMail2048',\
                       host='smtp.163.com',)
say_some = """hello world"""

mail_ob.send('1140880507@qq.com', 'just test', say_some)

