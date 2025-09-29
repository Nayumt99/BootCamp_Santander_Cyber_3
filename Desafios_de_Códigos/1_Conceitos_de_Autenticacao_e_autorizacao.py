entrada = input()

def descrever_conceito(conceito):
  if conceito == "Autenticação":
    return "Verificação da identidade de um usuário"
    
  # COMPLETANDO A FUNÇÃO:
  elif conceito == "Autorização":
    return "Permissão para acessar recursos específicos"

  elif conceito == "MFA":
    return "Verificação usando múltiplos fatores de segurança"

  elif conceito == "OAuth":
    return "Padrão aberto para delegar acesso sem compartilhar senha"

print(descrever_conceito(entrada))
