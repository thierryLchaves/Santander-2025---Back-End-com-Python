class Cachorro:
    def __init__(self,nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def latir(self):
        print("AuAuau")

    def __del__(self):
        print("Removendo a instância da classe.")

# def criar_cachorro():
#     c = Cachorro("Zeus","Branco e Preto",False)
#     print(c.nome)

c = Cachorro("Chappie","amaralo")

c.latir()
print("Hello World!")
del c
print("Hello World!")
print("Hello World!")
print("Hello World!")
# criar_cachorro()