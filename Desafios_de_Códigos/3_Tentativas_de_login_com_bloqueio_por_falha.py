entrada = input().strip()  

# Divide a string em uma lista, removendo espaços e mantendo tudo minúsculo por segurança
tentativas = [item.strip().lower() for item in entrada.split(',')]

# Inicializa o contador de falhas consecutivas
falhas_consecutivas = 0

# A flag é usada para indicar se o loop terminou normalmente (Acesso Normal) ou com break (Conta Bloqueada)
conta_bloqueada = False

# TODO: Percorra cada tentativa da lista:
for tentativa in tentativas:
    if tentativa == "falha":
        # TODO: Incremente se for uma falha:
        falhas_consecutivas += 1
        
        if falhas_consecutivas >= 3:
            # Imprime e encerra se houver 3 ou mais falhas seguidas
            conta_bloqueada = True
            break
    else:
        # Se for sucesso, reinicia o contador
        falhas_consecutivas = 0  

# Verifica o resultado
if conta_bloqueada:
    print("Conta Bloqueada")
else:
    # Se o loop NÃO for interrompido por um break, retorne, Acesso Normal:
    print("Acesso Normal")
