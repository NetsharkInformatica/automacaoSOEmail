from email.message import EmailMessage
import smtplib
import ssl

senha= open('senha','r').read()
from_email='aulas.python.netshark@gmail.com'
to_email='heliotome@netshark.com.br'
subject= 'curso de automação com python a partir de um arquivo txt'
body=open('dados/index.html.txt','r',encoding='utf-8').read()


message= EmailMessage()
message['From']=from_email
message['To']=to_email
message['Subject']=subject
#message['Body']= body
message.set_content(body,subtype='html')
safe = ssl.create_default_context()

#envio de email
with  smtplib.SMTP_SSL('smtp.gmail.com',465, context=safe) as smtp:
    smtp.login(from_email,senha)
    smtp.sendmail(
        from_email,
        to_email,
        message.as_string()
    )

