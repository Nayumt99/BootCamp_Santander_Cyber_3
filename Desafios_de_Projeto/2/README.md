# 🛡️ Malware Simulado Educacional com Python

**Projeto Prático de Segurança Cibernética**

Este repositório contém projetos em Python que simulam, em um ambiente **100% controlado e seguro**, o comportamento de malwares comuns como **Ransomware** e **Keylogger**. O objetivo principal é **educacional**: compreender o funcionamento interno dessas ameaças para desenvolver estratégias de **detecção, mitigação e defesa**.

⚠️ **AVISO LEGAL IMPORTANTE:**
Este código é estritamente para **fins educacionais e de pesquisa em segurança**. **NUNCA** execute ou adapte este código para atividades maliciosas ou em sistemas não autorizados. O uso indevido deste material é de inteira responsabilidade do usuário. A ética e a legalidade são primordiais no campo da cibersegurança.

---

## 🚀 Desafios Implementados

### 1. Ransomware Simulado (Pasta `1-Ransomware-Simulado/`)

Simulação de um ataque de sequestro de dados:

- **Funcionalidade:** Criptografa um conjunto específico de arquivos de teste usando um algoritmo seguro (e.g., `Fernet` da biblioteca `cryptography`).
- **Recursos:**
    - `ransomware_simulado.py`: Script para gerar a chave e criptografar os arquivos de teste.
    - `descriptografador.py`: Script para reverter o processo de criptografia.
    - Geração de uma "mensagem de resgate" simulada.

### 2. Keylogger Simulado (Pasta `2-Keylogger-Simulado/`)

Simulação de captura de entradas do teclado:

- **Funcionalidade:** Captura as teclas digitadas pelo usuário e as registra em um arquivo local (`logs/keystrokes_log.txt`).
- **Recursos:**
    - `keylogger_simulado.py`: Script principal de escuta e registro (utilizando bibliotecas como `pynput`).
    - `enviar_logs.py`: Script simulado para envio furtivo de logs (e.g., usando `smtplib` para e-mail - **Requer configuração de credenciais, que NUNCA devem ser salvas no código e muito menos no GitHub!**).

---

## 🧠 Reflexão sobre Defesa (Pasta `3-Defesa-Mitigacao/`)

O foco deste projeto é a defesa. Na pasta `3-Defesa-Mitigacao/`, você encontrará o arquivo `Estrategias_de_Defesa.md` que detalha:

- **Medidas Preventivas contra Ransomware:** Backup 3-2-1, segmentação de rede, políticas de acesso.
- **Medidas Preventivas contra Keylogger:** Uso de teclados virtuais, detecção de APIs de escuta, Monitoramento de tráfego de rede (exfiltração de dados).
- **Ferramentas e Conceitos:** Uso de Sandboxing (Ambientes Virtuais), Firewalls, Antivírus (Análise Heurística) e, o mais importante, **Conscientização do Usuário (Phishing)**.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.x
- **Bibliotecas Principais:**
    - `cryptography` (Para criptografia/descriptografia do Ransomware)
    - `pynput` (Para a escuta de teclado do Keylogger)
    - `smtplib` (Simulação de envio de logs)

### Como Executar

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SeuUsuario/Malware-Simulado-Educacional-Python.git](https://github.com/SeuUsuario/Malware-Simulado-Educacional-Python.git)
   cd Malware-Simulado-Educacional-Python
   ````

2. **Crie um ambiente virtual (Recomendado):**
  ````bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# ou
.\venv\Scripts\activate   # Windows
````

3. **Instale as dependências:**
 ````bash
pip install -r requirements.txt
````

4. **Execute os scripts (APENAS em seu ambiente de teste):**
 ````bash
Ransomware: python 1-Ransomware-Simulado/ransomware_simulado.py
Keylogger: python 2-Keylogger-Simulado/keylogger_simulado.py
````


## 🎓 Conclusão e Aprendizados
Este projeto foi fundamental para entender a cadeia de ataque desses malwares. A principal lição é que o conhecimento sobre o ataque é a melhor ferramenta para construir uma defesa robusta. A flexibilidade do Python torna a simulação de malwares acessível, reforçando a importância do uso ético da programação no campo da segurança.
