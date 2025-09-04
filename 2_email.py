from email.message import EmailMessage
import smtplib
import ssl

# Configurações - use apenas UM email como remetente
from_email = 'aulas.python.netshark@gmail.com'
to_email = 'heliotome@netshark.com.br,netsharkinformatica@gmail.com'



# Lê a SENHA DE APP (não a senha normal)
try:
    senha= open('senha','r').read().strip()
    # with open('pass', 'r') as f:
    #     senha_app = f.read().strip()
except FileNotFoundError:
    print("❌ Arquivo 'pass' não encontrado!")
    print("👉 Crie um arquivo chamado 'pass' com a SENHA DE APP")
    exit()

subject = 'curso de automação com python'
body = '''
aprendendo a criar automações com python.
a melhor maneira de prever o futuro, é criá-lo
'''

# Criar mensagem
message = EmailMessage()
message['From'] = from_email
message['To'] = to_email
message['Subject'] = subject
message.set_content(body)

# Configuração SSL
safe = ssl.create_default_context()

# Envio de email
try:
    print("🔗 Conectando ao servidor SMTP...")
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
        print("🔐 Logando com Senha de App...")
        smtp.login(from_email, senha)
        print("📤 Enviando email...")
        smtp.send_message(message)
        print("✅ Email enviado com sucesso!")
        
except smtplib.SMTPAuthenticationError:
    print("❌ Erro de autenticação. Verifique:")
    print("   - A verificação em duas etapas está ATIVADA?")
    print("   - Você gerou uma SENHA DE APP (não a senha normal)?")
    print("   - A senha no arquivo 'pass' está correta?")
    
except Exception as e:
    print(f"❌ Erro: {e}")