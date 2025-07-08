def dizer_oi(nome):
    return f"Oi {nome}"

def incentivar_aprender(nome):
    return f"Oi {nome}, vamos aprender Python juntos!"

def mensagem_para_thierry(funcao_mensagem):
    return funcao_mensagem("Thierry")


print(mensagem_para_thierry(dizer_oi))
print(mensagem_para_thierry(incentivar_aprender))