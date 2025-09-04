from email.message import EmailMessage
import smtplib
import ssl
import mimetypes

senha= open('senha','r').read()
from_email='aulas.python.netshark@gmail.com'
to_email='heliotome@netshark.com.br'
subject= 'curso de automação com html e anexo'
body=open('dados/index.html.txt','r',encoding='utf-8').read()


message= EmailMessage()
message['From']=from_email
message['To']=to_email
message['Subject']=subject
#message['Body']= body
message.set_content(body,subtype='html')
safe = ssl.create_default_context()

anexo= 'dados/mussum.jpg'
mime_type, mime_subtype = mimetypes.guess_type(anexo)

if mime_type:
    maintype, subtype = mime_type.split('/', 1)
else:
    maintype, subtype = 'application', 'octet-stream'

# with open(anexo,'rb') as a:
#     message.add_attachment(
#         a.read(),
#         maintype=mime_type.split('/')[0],  # Extrai apenas o tipo principal (ex: 'image')
#         subtype=mime_type.split('/')[1],   # Extrai apenas o subtipo (ex: 'jpeg')
#         filename=anexo
#     )
with open(anexo, 'rb') as img:
    message.add_attachment(
        img.read(),
        maintype=maintype,
        subtype=subtype,
        filename='mussum.jpg',
        cid='mussum_image'  # Content-ID para referência no HTML
    )
#envio de email
with  smtplib.SMTP_SSL('smtp.gmail.com',465, context=safe) as smtp:
    smtp.login(from_email,senha)
    smtp.sendmail(
        from_email,
        to_email,
        message.as_string()
    )

