# Lista de produtos disponíveis no estoque
estoque = ["Camiseta", "Calça", "Tênis", "Boné", "Jaqueta"]

# Entrada do usuário
produto = input().strip()

result = [prod for prod in estoque if prod == produto]
if result:
    print("Produto disponível")
else:
    print("Produto esgotado")
