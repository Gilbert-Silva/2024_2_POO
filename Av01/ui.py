from atleta import Atleta, Atletas
from treino import Treino, Treinos
from datetime import datetime, timedelta

class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.atleta_inserir()
            if op == 2: UI.atleta_listar()
            if op == 3: UI.treino_inserir()
            if op == 4: UI.treino_listar()
            if op == 5: UI.atleta_mais_rapido()
            if op == 6: UI.treino_mais_rapido()
    @staticmethod
    def menu():
        print("1-Inserir Atleta  2-Listar Atleta  3-Inserir Treino  4-Listar Treino  5-Atleta mais rápido  6-Treino mais rápido  9-Fim")
        return int(input("Escolha uma opção: "))
    @staticmethod
    def atleta_inserir():
        id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        nasc = datetime.strptime(input("Informe o nascimento: "), "%d/%m/%Y")
        a = Atleta(id, nome, nasc)
        Atletas.inserir(a)
    @staticmethod
    def atleta_listar():
        for atleta in Atletas.listar(): print(atleta)
    @staticmethod
    def treino_inserir():
        id = int(input("Informe o id: "))
        id_atleta = int(input("Informe o id do atleta: "))
        data = datetime.strptime(input("Informe a data: "), "%d/%m/%Y")
        dist = int(input("Informe a distância em metros: "))
        tempo = input("Informe o tempo em hh:mm:ss: ")
        h, m, s = map(int, tempo.split(":"))
        a = Treino(id, id_atleta, data, dist, timedelta(hours=h, minutes=m, seconds=s))
        Treinos.inserir(a)
    @staticmethod
    def treino_listar():
        for treino in Treinos.listar(): print(treino)   
    @staticmethod
    def atleta_mais_rapido():
        treinos = Treinos.listar()
        menor = treinos[0]
        for treino in treinos: 
            if treino.pace() < menor.pace(): menor = treino
        print(menor.get_id_atleta())
    @staticmethod
    def treino_mais_rapido():
        id_atleta = int(input("Informe o id do atleta: "))
        treinos = Treinos.listar()
        for treino in treinos:
            if treino.get_id_atleta() == id_atleta: 
                menor = treino
                break
        for treino in treinos: 
            if treino.get_id_atleta() == id_atleta: 
                if treino.pace() < menor.pace(): menor = treino
        print(menor)

UI.main()
