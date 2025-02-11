class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) :
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)    
    
aluno_01 = Estudante("Jonatan", 1)
aluno_02 = Estudante("Gui", 2)    

mostrar_valores(aluno_01, aluno_02)

aluno_01.matricula = 6
mostrar_valores(aluno_01, aluno_02)