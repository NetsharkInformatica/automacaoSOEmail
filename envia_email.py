from email.message import EmailMessage
import smtplib
import ssl


senha= open('senha','r').read()
#print(senha)
from_email='aulas.python.netshark@gmail.com'
to_email='heliotome@netshark.com.br'
subject= 'curso de automação com python'
body= '''
aprendendo a criar automações com pyton.
a melhor maneira de prever o futuro, é cria lo
'''
message= EmailMessage()
message['From']=from_email
message['To']=to_email
message['Subject']=subject
#message['Body']= body
message.set_content(body)
safe = ssl.create_default_context()

#envio de email
with  smtplib.SMTP_SSL('smtp.gmail.com',465, context=safe) as smtp:
    smtp.login(from_email,senha)
    smtp.sendmail(
        from_email,
        to_email,
        message.as_string()
    )



