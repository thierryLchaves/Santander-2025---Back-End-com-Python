class Bicicleta:
    def __init__(self,cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        # self.marcha = 1

    def buzinar(self):
        print("PLim plim")

    def parar(self):
        print("parando a bicicleta")
        print("Bicicleta parada !")
    
    def correr(self):
        print("vruuuuuum")

    # def trocar_marchar(self,nro_marcha):
    #     print("Trocando marcha")
    #     def _trocar_marchar(nr_marcha):
    #         if nr_marcha > self.marcha:
    #             print("Marcha trocada")
    #         else:
    #             print(" Não foi possível trocar de marcha...")

    # def __str__(self):
    #     return f"Bicicleta: cor={self.cor},modelo={self.modelo}, ano={self.ano}, valor={self.valor}"

    def __str__(self):
        return f"{self.__class__.__name__}:{' , '.join([f'{chave}={valor}'for chave, valor in self.__dict__.items()])}" 
    
b1 = Bicicleta("Vermelha","caloi",2022,600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor,b1.ano,b1.valor)

b2 = Bicicleta("verde","monark",2000,189)
print(b2)