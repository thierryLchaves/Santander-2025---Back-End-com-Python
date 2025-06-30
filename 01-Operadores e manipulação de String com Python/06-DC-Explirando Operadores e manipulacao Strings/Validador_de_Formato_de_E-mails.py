# Entrada do usuário
email = input().strip()
dominios = [
'@gmail.com', '@outlook.com'
]


def verif_posicao():
    contem = 0
    if email[0] == '@':
      contem += 1
    elif email[-1] == '@':
      contem += 1
    return contem

def verif_dominio():
    contem = 0
    if dominios[0] in email:
        contem += 1
    elif dominios[1] in email:
        contem += 1

    return contem

def verif_espaco():
    contem = 0
    if ' ' in email:
      contem += 1

    return contem



if verif_posicao() == 0 and verif_dominio() > 0 and verif_espaco() == 0:
    print("E-mail válido")
else:
  print("E-mail inválido")
