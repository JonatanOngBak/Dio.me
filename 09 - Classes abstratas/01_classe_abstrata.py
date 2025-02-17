from abc import ABC, abstractmethod, abstractproperty

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
        return 


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
        print("Ligada!")

    def desligar(self):
        print("Desligano a TV...")
        print("Desligado!")

    @property
    def marca(self):
        return "LG"

class ControleArcondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o ar Condicionado...")
        print("Ligado!")

    def desligar(self):
        print("Desligano o ar Condicionado...")
        print("Desligado!")

    @property
    def marca(self):
        return "Philco"


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)


controle = ControleArcondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)