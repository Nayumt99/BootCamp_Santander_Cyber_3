# Estratégias de Defesa e Mitigação contra Ransomware e Keyloggers

O foco primário da segurança cibernética está na defesa. Entender o ataque é o primeiro passo para construir barreiras eficazes.

## 1. Defesa Contra Ransomware

O Ransomware explora a vulnerabilidade dos dados e a urgência de acessá-los.

| Estratégia | Detalhamento | Nível de Prevenção |
| :--- | :--- | :--- |
| **Backup 3-2-1** | Manter **3** cópias dos dados, em **2** tipos de mídia diferentes, e **1** cópia **off-site/offline** (air-gapped) que não pode ser acessada pelo malware. | Mitigação de Danos (Recuperação) |
| **Segmentação de Rede** | Limitar o acesso do usuário e do dispositivo infectado apenas às áreas essenciais. Impede que o Ransomware se espalhe lateralmente na rede (do desktop para o servidor). | Contenção |
| **Políticas de Acesso (ACLs)** | Usar o princípio do **menor privilégio**. Usuários não devem ter permissão de escrita em diretórios que não lhes pertencem, como pastas de servidor de toda a empresa. | Prevenção |
| **Softwares de Detecção** | Utilizar EDRs (Endpoint Detection and Response) ou Antivírus que monitorem o **comportamento** (heurística), identificando a varredura e a abertura em massa de arquivos para criptografia. | Detecção e Bloqueio |

## 2. Defesa Contra Keyloggers

Keyloggers exploram a confiança no sistema operacional para interceptar entradas.

| Estratégia | Detalhamento | Nível de Prevenção |
| :--- | :--- | :--- |
| **Monitoramento de Processos** | Sistemas de segurança devem procurar por processos não assinados ou suspeitos que tentam se anexar a APIs de teclado (hooks) do sistema operacional. | Detecção |
| **Autenticação Multifator (MFA)** | Embora o Keylogger possa capturar a senha, o MFA exige uma segunda forma de verificação (código no celular), tornando a senha roubada inútil por si só. | Mitigação de Danos |
| **Monitoramento de Tráfego (Exfiltração)** | Firewalls e sistemas de prevenção de intrusão (IPS) devem monitorar o tráfego de saída incomum, especialmente conexões não autenticadas ou suspeitas via protocolos como SMTP (porta 587 ou 25). | Detecção de Exfiltração |
| **Uso de Teclados Virtuais** | Para senhas críticas (bancos), o uso de teclados virtuais na tela dificulta a captura, pois o Keylogger registra apenas cliques do mouse, e não as teclas. | Prevenção |

## 3. Pilares Comuns de Defesa (Princípios Gerais)

### A. Conscientização do Usuário (O Elo Mais Forte/Fraco)
Quase todos os malwares dependem de uma ação humana para serem instalados (clicar em um anexo de *phishing* ou baixar um software pirata).
- **Treinamento:** Educar os usuários sobre iscas comuns (urgência, autoridade falsa, ofertas inacreditáveis).
- **Verificação:** Ensinar a verificar cabeçalhos de e-mail e links antes de clicar.

### B. Sandboxing e Ambientes Virtuais
- **Sandboxing:** Executar anexos de e-mail ou programas suspeitos em um ambiente isolado (sandbox) que simula o sistema operacional, mas sem acesso aos arquivos reais ou à rede interna.
- **Máquinas Virtuais (VMs):** Usar VMs dedicadas para testes e navegação de risco, garantindo que o malware fique contido ali.

### C. Gestão de Patches e Vulnerabilidades
- Manter o Sistema Operacional e todos os softwares (navegadores, leitores de PDF) **atualizados**. Malwares frequentemente exploram vulnerabilidades conhecidas (exploits) que já foram corrigidas pelos fabricantes.
