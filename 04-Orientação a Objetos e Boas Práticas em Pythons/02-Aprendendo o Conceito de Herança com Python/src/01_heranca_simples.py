class veiculo:
    def __init__(self,cor, placa, numero_de_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_de_rodas = numero_de_rodas  
    
    def ligar_motor(self):
        print("Ligando o motor")
    
    def __str__(self):
        return f"{self.__class__.__name__}:{' , '.join([f'{chave} = {valor}'for chave, valor in self.__dict__.items()])}" 


class Motocicleta(veiculo):
    pass

class Carro(veiculo):
    pass

class Caminhao(veiculo):    
    def __init__(self,cor,placa,numero_de_rodas, carregado):
        super().__init__(cor, placa, numero_de_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim'if self.carregado else 'Não'} está carregado")

moto = Motocicleta("vermelha", "ABC-1234", 2)
caminhao = Caminhao("azul", "LMN-9012", 8,True)
carro = Carro("Branco", "XYZ-5678", 4)

print(caminhao)
print(moto)
print(carro)

