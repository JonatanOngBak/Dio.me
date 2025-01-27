class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a classe...")

    def falar(self):
        print("auau")


def criar_cachorro():
    c = Cachorro("Aladin", "branco", False)
    print(c.nome)

c = Cachorro("Chapie", "Amarelo")
c.falar()
