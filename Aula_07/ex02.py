class Aluno:
    def __init__(self, nome, mat):
        self.__nome = nome
        self.__matricula = mat
    def __str__(self):
        return f"{self.__nome} - {self.__matricula}"
        
class Turma:
    def __init__(self, disciplina):
        self.__disciplina = disciplina
        self.__alunos = []
    def inserir(self, aluno):
        self.__alunos.append(aluno)   
    def listar(self):
        return self.__alunos     
    def __str__(self):
        return f"{self.__disciplina} tem {len(self.__alunos)} aluno(s)" 

class UI:
    @staticmethod
    def menu():
        print("1-Nova turma, 2-Inserir aluno, 3-Listar alunos, 9-Fim")
        return int(input("Informe uma opção: "))
    @staticmethod
    def main():
        op = 0
        turma = None
        while op != 9:
            op = UI.menu()
            if op == 1: turma = UI.nova_turma()
            if op == 2: 
                if turma == None: print("Nenhuma turma criada!")
                else: UI.inserir_aluno(turma)
            if op == 3:
                if turma == None: print("Nenhuma turma criada!")
                else: UI.listar_alunos(turma)
    @staticmethod
    def nova_turma():
        d = input("Informe o nome da disciplina: ")
        turma = Turma(d)
        return turma
    @staticmethod
    def inserir_aluno(turma):
        n = input("Informe o nome do aluno: ")
        m = input("Informe a matrícula: ")
        aluno = Aluno(n, m)
        turma.inserir(aluno)
    @staticmethod
    def listar_alunos(turma):
        print(turma)
        for aluno in turma.listar(): print(aluno)

UI.main()

"""    
a = Aluno("Gilbert", "1234")
b = Aluno("Eduardo", "4321")
x = Turma("Tads")
x.inserir(a)
x.inserir(b)
for aluno in x.listar(): print(aluno)
print(x)
"""

       