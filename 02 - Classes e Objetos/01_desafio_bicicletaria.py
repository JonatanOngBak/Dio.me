class Bicicleta:
    def __init__(self,cor ,modelo ,ano ,valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    def buzinar(self):
        print("Plin Plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!...")

    def correr(self):
        print("Vrummm...")        

    def trocar_marcha(nro_marcha):
        print(nro_marcha)
        print("Marcha trocada...")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


#b1 = Bicicleta("vermelha", "Caloi", 2025, 600)    
#b1.buzinar()
#b1.correr()
#b1.parar()
#print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 189)
print(b2)