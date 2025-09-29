# 🛡️ Desafio de Projeto: Simulação de Ataque Brute Force com Kali Linux e Medusa

<p align="center">
  <img src="https://assets.dio.me/C_w739DMTY1XPvnkcaSY7doWFM9I5MREIuft-gfwJDY/f:webp/h:120/q:80/L3RyYWNrcy83MGI2Y2EwOC0xZDdlLTQxNTctYmI0OC05NmMxMTY0ZmQ3ZTcucG5n" alt="Logo/Banner do Bootcamp Cibersegurança">
</p>

Este repositório documenta a execução do Desafio de Projeto prático do **Bootcamp Santander Code Girls - Cyber Security Expert (DIO)**. O foco é simular e documentar um cenário de **ataque de força bruta** contra diferentes serviços, utilizando o **Kali Linux** e a ferramenta **Medusa** em um ambiente de laboratório controlado.

O objetivo principal é exercitar a mentalidade de auditoria de segurança (Hacking Ético) e propor medidas eficazes de prevenção.

---

## 🎯 Objetivos de Aprendizagem Demonstrados

Ao longo deste projeto, demonstrei as seguintes competências:

1.  **Conceitos de Ataques:** Compreensão de ataques de força bruta, *password spraying* e ataques a serviços específicos (FTP, Web, SMB).
2.  **Uso de Ferramentas:** Proficiência na configuração do **Kali Linux** e na utilização da ferramenta **Medusa** para auditoria em ambiente controlado.
3.  **Documentação:** Habilidade em documentar processos técnicos (comandos, resultados e configurações) de forma clara e estruturada.
4.  **Mitigação:** Reconhecimento de vulnerabilidades exploradas e proposta de medidas eficazes de mitigação.
5.  **Portfólio Técnico:** Utilização do **GitHub** como portfólio para compartilhar a jornada e as evidências técnicas.

---

## ⚙️ Configuração do Ambiente de Laboratório

Para manter a integridade e a segurança, todos os testes foram executados em um ambiente de máquinas virtuais (VMs) isolado, simulando um laboratório de teste de invasão.

| Componente | Detalhe | Rede |
| :--- | :--- | :--- |
| **Atacante (Attacker VM)** | **Kali Linux** (Ferramenta: Medusa) | `Host-Only` (Isolada) |
| **Alvo (Target VM)** | **Metasploitable 2** e **DVWA** | `Host-Only` (Isolada) |
| **Ferramenta de Virtualização** | **VirtualBox** | N/A |

### Estrutura de Pastas:

* `/images`: Capturas de tela organizadas de cada cenário.
* `/wordlists`: Arquivos de texto simples utilizados para os testes.

---

## 🧪 Cenários de Ataque e Execução com Medusa

Os testes foram realizados em diferentes protocolos para demonstrar a aplicabilidade da força bruta em diversos contextos.

### Cenário 1: Ataque de Força Bruta em Serviço FTP

Este teste explorou o serviço FTP do Metasploitable 2, que tipicamente não implementa bloqueio de tentativas de login.

| Detalhe | Valor |
| :--- | :--- |
| **Serviço Alvo** | FTP (Porta 21) |
| **Wordlists** | `users.txt` (Usuários comuns) e `passwords.txt` (Senhas fracas) |

**Comando Medusa Utilizado:**

```
# Tentativa com lista de usuários e lista de senhas
medusa -H 192.168.56.102 -U /path/to/users.txt -P /path/to/passwords.txt -M ftp

````

### Cenário 2: Password Spraying em SMB

O Password Spraying testa uma única senha comum em uma lista de múltiplos usuários, sendo eficiente para ambientes com políticas de lockout de contas.

Serviço Alvo: SMB (Porta 445)

Ataque: Password Spraying (uma senha contra muitos usuários).

**Comando Medusa Utilizado:**


````
medusa -H [IP_ALVO] -U /path/to/users_smb.txt -p [SENHA_ÚNICA_FRACA] -M smb
````

### Cenário 3: Ataque a Formulário Web (DVWA)

Simulação de ataque automatizado via HTTP POST contra a página de login de uma aplicação web vulnerável.

Serviço Alvo: HTTP (Aplicação Web DVWA)

Ataque: Força Bruta contra campos de formulário.

**Comando Medusa Utilizado (Exemplo de Mapeamento):**

````
# Mapeamento do POST request para o Medusa, ajustando os parâmetros USER e PASS
medusa -H [IP_ALVO] -U /path/to/users.txt -P /path/to/passwords.txt -M http -m DIR:/
````
