from abc import ABC,abstractmethod,abstractproperty

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass

class Controletv(ControleRemoto):
    
    def ligar(self):
        print("ligando TV...")
        print("Ligado!")

    def desligar(self):
        print("Desligando a TV...")
        print("Desligada!")

    @property
    def marca(self):
        return "LG"

class ControleArCondicionado(ControleRemoto):

    def ligar(self):
        print("Ligando o ar condicionado ")
        print("Ligado!")

    
    def desligar(self):
        print("Desligando o ar...")
        print("Desligado!")

    @property
    def marca(self):
        return "Philco"

controle = Controletv()
controle.ligar()
controle.desligar()
print(controle.marca)


controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)