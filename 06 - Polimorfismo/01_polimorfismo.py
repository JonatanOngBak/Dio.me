class Passaro:
    def voar(self):
        print("voando...")

class Pardal(Passaro):
    def voar(self):
        super().voar()

class Avestrus(Passaro):
    def voar(self):
        print("Avestrus não pode voar")

def plano_voo(obj):
    obj.voar()


p1 = Pardal()
p2 = Avestrus()

plano_voo(p1)
plano_voo(p2)
