class Pedido:
    def __init__(self):
        self.itens = []  
    

    def adicionar_item(self,nome,preco):
        self.itens.append((nome,preco))
          
    def calcular_total(self):
        preco = [float(preco) for nome, preco in self.itens]
        soma = sum(preco)
        return soma


quantidade_pedidos = int(input().strip())
soma = 0
pedido = Pedido()

for _ in range(quantidade_pedidos):
    entrada = input().strip()
    nome, preco = entrada.rsplit(" ", 1)
    pedido.adicionar_item(nome,preco)
    soma = pedido.calcular_total()
    
print(f"{soma:.2f}")
