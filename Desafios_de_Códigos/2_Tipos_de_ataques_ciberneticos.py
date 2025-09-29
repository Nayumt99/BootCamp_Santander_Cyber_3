entrada = input()

def descrever_ataque(ataque):
  if ataque == "Phishing":
    return "Enganar usuários para roubar informações sensíveis"
    
  # COMPLETANDO A FUNÇÃO:
  elif ataque == "DDoS":
    return "Atacar um serviço com muitos acessos para derrubá-lo"

  elif ataque == "Malware":
    return "Software malicioso projetado para causar danos"

  elif ataque == "Engenharia Social":
    return "Manipulação psicológica para obter acesso ou dados"

print(descrever_ataque(entrada))
