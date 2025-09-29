def verificar_comando(comando):
    # Caracteres suspeitos para injeção de comando
    caracteres_suspeitos = [';', '&', '|', '$']
    
    # TODO: Verifique se algum dos caracteres suspeitos está no comando:
    for char in caracteres_suspeitos:
        if char in comando:
            return "Comando Suspeito"
    
    return "Comando Seguro"

# Entrada do usuário
comando_usuario = input()

# TODO: Retorne o resultado da verificação:
print(verificar_comando(comando_usuario))
