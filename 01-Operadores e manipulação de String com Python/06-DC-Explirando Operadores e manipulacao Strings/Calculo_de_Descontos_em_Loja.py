# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip()

for desconto in descontos:
    if cupom == desconto:
      preco -= preco * descontos.get(cupom)
    elif cupom != desconto or cupom == "SEM_DESCONTO":
        preco

print(F"{preco:.2f}")
    