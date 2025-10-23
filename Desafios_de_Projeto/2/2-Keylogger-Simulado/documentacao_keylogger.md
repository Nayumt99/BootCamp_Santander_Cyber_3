# Documentação do Keylogger Simulado

## 1. Objetivo Educacional
Simular a captura de dados do teclado e a exfiltração desses dados via e-mail para entender:
1.  Como um programa pode interceptar eventos de baixo nível do sistema operacional (teclado).
2.  A diferença entre teclas de caracteres e teclas especiais (`Shift`, `Ctrl`, `Enter`).
3.  A mecânica de exfiltração de dados (envio dos logs) e a importância do SMTP.

## 2. Tecnologia e Mecanismo
- **Linguagem:** Python
- **Biblioteca de Escuta:** `pynput`. Esta biblioteca permite controlar e monitorar dispositivos de entrada, como mouse e teclado, em diferentes sistemas operacionais.

## 3. Fluxo de Execução (`keylogger_simulado.py`)
1.  **Listener:** O `keyboard.Listener` é iniciado, criando um loop que aguarda eventos do teclado.
2.  **Tratamento de Teclas:** O *callback* `on_press` é chamado a cada pressionamento:
    - Teclas de caracteres são registradas diretamente (`key.char`).
    - Teclas especiais (como `Shift` ou `Enter`) são formatadas para serem legíveis, e.g., `[ENTER]`, `[SHIFT]`.
3.  **Registro:** As teclas são apensadas (adicionadas) ao arquivo `keystrokes_log.txt`.
4.  **Furtividade (Simulada):** O script foi limitado a 20 entradas e pode ser parado com `ESC` para fins de teste. Em um ataque real, ele seria executado como um processo em *background* sem interface gráfica ou saídas de terminal.

## 4. Exfiltração de Dados (`enviar_logs.py`)
A exfiltração é o ato de enviar os logs capturados para o atacante.
1.  **Leitura:** O script lê o conteúdo de `keystrokes_log.txt`.
2.  **Composição de E-mail:** O conteúdo do log é encapsulado em um objeto `MIMEMultipart`.
3.  **Envio:** O protocolo **SMTP (Simple Mail Transfer Protocol)** é usado:
    - O script conecta-se ao servidor SMTP (e.g., Gmail, Outlook).
    - `server.starttls()` é usado para criptografar a sessão de e-mail (necessário em quase todos os provedores modernos).
    - As credenciais do atacante são usadas para autenticação (`server.login()`).
    - O e-mail é enviado.
4.  **Limpeza:** Após o envio, o arquivo de log local é esvaziado, simulando um Keylogger que limpa seu rastro ou envia logs em intervalos regulares.
