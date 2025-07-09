def menssagem(nome):
    print("Excecutando nome")
    return f'oi {nome}'

def mensagem_longa(nome):
    print('Executando mensagem longa')
    return f'Olá tudo bem como você {nome}'

def executar(funcao,nome):
    print('Executando a executar')
    return funcao(nome)


print(executar(menssagem,"thierry"))
print(executar(mensagem_longa,"thierry"))