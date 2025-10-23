# Documentação do Ransomware Simulado

## 1. Objetivo Educacional
Simular o processo de sequestro e recuperação de dados para entender:
1.  Como a chave de criptografia é gerada e armazenada (ou enviada).
2.  Como o malware identifica arquivos alvo (pelas extensões).
3.  O impacto da criptografia e a necessidade da chave para reversão.

## 2. Tecnologia e Algoritmo
- **Linguagem:** Python
- **Biblioteca de Criptografia:** `cryptography.fernet`
- **Algoritmo:** **Fernet**. É um formato de criptografia simétrica baseado em AES-128 em modo CBC (Cipher Block Chaining) com HMAC (Hash-based Message Authentication Code). Isso garante tanto a **confidencialidade** (AES) quanto a **autenticidade** (HMAC), dificultando a adulteração dos dados criptografados.

## 3. Fluxo de Execução (`ransomware_simulado.py`)
1.  **Geração de Chave:** Uma chave aleatória e única é gerada usando `Fernet.generate_key()`.
2.  **Persistência da Chave:** A chave é salva localmente em `chave_secreta.key` (Em um ataque real, essa chave seria enviada para o C2 - *Command and Control*).
3.  **Varredura:** O script percorre a pasta `arquivos_teste`.
4.  **Criptografia:** Para cada arquivo com extensão alvo (`.txt`, `.pdf`, etc.):
    - O conteúdo é lido em bytes.
    - É criptografado usando o objeto `Fernet`.
    - O conteúdo criptografado é salvo, **sobrescrevendo** o arquivo original.
5.  **Extensão Maliciosa:** O arquivo é renomeado com a extensão `.locked` para indicar o sequestro.
6.  **Mensagem de Resgate:** Um arquivo de texto (`LEIA_ME_RESGATE.txt`) é criado com instruções de "pagamento".

## 4. Reversão (`descriptografador.py`)
O processo de reversão exige a chave gerada.
1.  A chave é lida de `chave_secreta.key`.
2.  O script varre a pasta procurando arquivos com a extensão `.locked`.
3.  O conteúdo criptografado é lido e passado para o método `fernet.decrypt()`.
4.  O conteúdo original é salvo, e a extensão `.locked` é removida, restaurando o arquivo.
