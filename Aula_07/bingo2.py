import random
class Bingo:
    def __init__(self, num_bolas):
        self.__num_bolas = num_bolas
        self.__bolas = list()
        if num_bolas < 1: raise ValueError("Número de bolas inválido")
    def proximo(self):
        if len(self.__bolas) == self.__num_bolas: return -1
        n = random.randint(1, self.__num_bolas)
        while n in self.__bolas: 
            n = random.randint(1, self.__num_bolas)
        self.__bolas.append(n)
        return n
    def sorteados(self):
        self.__bolas.sort()
        return self.__bolas    

class UI:
    jogo = None  # Atributo da classe - atributo estático - fora do __init__

    @staticmethod
    def menu():
        print("1-Novo jogo, 2-Sortear, 3-Sorteados, 9-Fim")
        return int(input("Informe uma opção: "))
    @classmethod
    def main(cls):
        op = 0
        jogo = None
        while op != 9:
            op = UI.menu()
            if op == 1: cls.jogo = UI.novo_jogo()
            if op == 2: UI.sortear()
            if op == 3: UI.sorteados()
    @staticmethod
    def novo_jogo():
        n = int(input("Informe o número de bolas: "))
        return Bingo(n)
    @classmethod
    def sortear(cls):
        n = cls.jogo.proximo()
        if n == -1: print("Fim do Jogo")
        else: print(n)
    @classmethod
    def sorteados(cls):
        print(cls.jogo.sorteados())        

UI.main()
    
