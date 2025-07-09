# def duplicar(func):
#     def envelope(*args, **kwargs):
#         func(*args,**kwargs)
#         func(*args,**kwargs)

#     return envelope

# @duplicar
# def aprender(tecnologia):
#     print(f"Estou aprendendo {tecnologia}")

# aprender("Pyhon")

# def meu_decorador(funcao):
#     def envelope(*args,**kwargs):
#         print("Faz algo antes de executar a função ")
#         resulta = funcao(*args,**kwargs)
#         print("Faz algo depois de executar a função ")
#         return resulta
#     return envelope

# @meu_decorador
# def ola_mundo(nome):
#     print(f"Olá mundo !{nome}")
#     return nome.upper()


# # ola_mundo = meu_decorador(ola_mundo)
# resultado = ola_mundo("Thierry")
# print(resultado)

import functools
def meu_decorador(funcao):
    @functools.wraps(funcao)
    def envelope(*args,**kwargs):
        funcao(*args,**kwargs)
    return envelope

@meu_decorador
def ola_mundo(nome):
    print(f"Olá mundo !{nome}")


print(ola_mundo.__name__)