from email.mime.text import MIMEText
import smtplib
from email.mime.multipart import MIMEMultipart, MIMEBase
from email.mime.image import MIMEImage
import os
import time
from email.mime.application import MIMEApplication


class  SendMail():
    def send_mail(self, user_list, subject, content,excel_path,excel_name):
        send_user = "931038157@qq.com"
        password = "pozsbymhxkombaja"
        email_host = "smtp.qq.com"
        user = "转角" + "<" + send_user + ">"

        m = MIMEMultipart()

        m_text = MIMEText(content, _subtype="plain",
                           _charset="utf-8")  # 此处的_subtype="plain",代表就是邮件类型，就是普通text邮件类型,如果是html就是html类型

        #excel_path="./datacofig/interface.xls"
        m_excel=MIMEApplication(open(excel_path,'rb').read())
        m_excel.add_header('Content-Disposition', 'attachment', filename=excel_name)


        m.attach(m_text)
        m.attach(m_excel)



        m["To"] = user_list
        m["from"] = user
        m["subject"] = subject

        server = smtplib.SMTP_SSL()
        server.connect(email_host)
        server.login(send_user, password)
        server.sendmail(user, user_list, m.as_string())
        server.close()

    def send_main(self, pass_list, fail_list):
        excel_path = "../datacofig/interface.xls"
        excel_name='api详情统计.xls'
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        count_num = pass_num + fail_num
        pass_result = "%.2f%%" % (pass_num / count_num * 100)
        fail_result = "%.2f%%" % (fail_num / count_num * 100)
        user_list = "yanlizhi@myhexin.com"
        subject = "接口自动化测试报告"
        content = "此处一共运行接口个数为%s个，通过个数为%s个，失败个数为%s个，通过率为%s，失败率为%s" % (
        count_num, pass_num, fail_num, pass_result, fail_result)
        self.send_mail(user_list, subject, content,excel_path,excel_name)


if __name__=="__main__":

    send=SendMail()
    send.send_main([1,2],[2])


