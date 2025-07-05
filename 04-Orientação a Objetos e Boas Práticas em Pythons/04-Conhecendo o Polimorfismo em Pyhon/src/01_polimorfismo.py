class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
       print("Pardal pode voar")

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")

# FIXME: EXEMPLO RUIM DO USO DE Herança PARA "GANHAR" o método voar
class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando")

def plano_de_voo(obj):
    obj.voar()


plano_de_voo( Pardal())
plano_de_voo(Avestruz())
plano_de_voo(Aviao())