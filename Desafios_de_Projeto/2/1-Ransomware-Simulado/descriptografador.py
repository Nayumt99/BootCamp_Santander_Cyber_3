import os
from cryptography.fernet import Fernet

# ----------------------------------------------------------------------
# SCRIPT DE DESCRIPTOGRAFIA (PARA REVERTER O TESTE DE RANSOMWARE)
# ----------------------------------------------------------------------

# 1. Definições de Caminho (as mesmas do script de criptografia)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TARGET_DIR = os.path.join(BASE_DIR, 'arquivos_teste')
KEY_FILE = os.path.join(BASE_DIR, 'chave_secreta.key')
EXTENSAO_LOCKED = '.locked'

def carregar_chave():
    """Carrega a chave do arquivo."""
    try:
        with open(KEY_FILE, 'rb') as key_file:
            return key_file.read()
    except FileNotFoundError:
        print(f"ERRO: Arquivo de chave '{KEY_FILE}' não encontrado. Execute o ransomware primeiro.")
        return None

def descriptografar_arquivo(caminho_bloqueado, fernet):
    """Lê, descriptografa e sobrescreve o arquivo."""
    try:
        with open(caminho_bloqueado, 'rb') as file:
            dados_criptografados = file.read()

        dados_descriptografados = fernet.decrypt(dados_criptografados)

        # 2. Renomeia o arquivo, removendo a extensão .locked
        caminho_original = caminho_bloqueado.replace(EXTENSAO_LOCKED, '')
        os.rename(caminho_bloqueado, caminho_original)

        # 3. Salva os dados originais
        with open(caminho_original, 'wb') as file:
            file.write(dados_descriptografados)
            
        print(f"[+] DESCRIPTOGRAFADO: {os.path.basename(caminho_original)}")

    except Exception as e:
        print(f"[!] Erro ao descriptografar {caminho_bloqueado}: {e}. Chave incorreta ou arquivo danificado.")

def reverter_ransomware_simulado():
    """Reverte a criptografia nos arquivos de teste."""
    print("--- INICIANDO REVERSÃO DE RANSOMWARE ---")
    chave = carregar_chave()
    
    if chave is None:
        return

    fernet = Fernet(chave)
    arquivos_bloqueados = 0

    # 4. Percorre a pasta alvo procurando arquivos .locked
    for arquivo in os.listdir(TARGET_DIR):
        caminho_completo = os.path.join(TARGET_DIR, arquivo)
        
        if os.path.isfile(caminho_completo) and caminho_completo.endswith(EXTENSAO_LOCKED):
            descriptografar_arquivo(caminho_completo, fernet)
            arquivos_bloqueados += 1
            
    if arquivos_bloqueados == 0:
        print("Nenhum arquivo .locked encontrado para descriptografar.")

    # 5. Remove a mensagem de resgate
    resgate_file = os.path.join(TARGET_DIR, 'LEIA_ME_RESGATE.txt')
    if os.path.exists(resgate_file):
        os.remove(resgate_file)
        print(f"[*] Mensagem de Resgate removida: {resgate_file}")

    print("\n--- REVERSÃO CONCLUÍDA. Verifique seus arquivos ---")

if __name__ == "__main__":
    reverter_ransomware_simulado()
