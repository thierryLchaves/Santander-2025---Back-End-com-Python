from datetime import datetime
class Veiculo:
    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano  = ano
    
    def verificar_antiguidade(self):
        ano_atual = datetime.now().year
        calculo =  ano_atual - self.ano 
        devolutiva = ''
        if calculo > 20:
            devolutiva = 'Veículo antigo'
        else:
            devolutiva = 'Veículo novo'
        return devolutiva

            
        
    

# Entrada direta
marca = input().strip()
modelo = input().strip()
ano = int(input().strip())

# Instanciando o objeto e verificando a antiguidade
veiculo = Veiculo(marca, modelo, ano)
print(veiculo.verificar_antiguidade())



