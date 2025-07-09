# def dizer_oi(nome):
#     return f"Oi {nome}"

# def incentivar_aprender(nome):
#     return f"Oi {nome}, vamos aprender Python juntos!"

# def mensagem_para_thierry(funcao_mensagem):
#     return funcao_mensagem("Thierry")


# print(mensagem_para_thierry(dizer_oi))
# print(mensagem_para_thierry(incentivar_aprender))

# def pai():
#     print("Escrevendo da pai() função")

#     def filho1():
#         print("Escrevendo da filho1() função")
    
#     def filho2():
#         print("Escrevendo da filho2() função")

#     filho1()
#     filho2()

# pai()

def calcular(operacao):
    def somar(a,b):
        return a+b
    def substrair(a,b):
        return a-b
    
    if operacao == "+":
        return somar
    else:
        return substrair

resultado = calcular("+")(1,3)

print(resultado)