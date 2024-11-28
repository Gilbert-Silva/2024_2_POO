from models.atleta import Atleta, Atletas
from models.treino import Treino, Treinos

class View:
    @staticmethod
    def atleta_inserir(id, nome, nasc):
        a = Atleta(id, nome, nasc)
        Atletas.inserir(a)
    @staticmethod
    def atleta_listar():
        return Atletas.listar()
    @staticmethod
    def treino_inserir(id, id_atleta, data, dist, tempo):
        a = Treino(id, id_atleta, data, dist, tempo)
        Treinos.inserir(a)
    @staticmethod
    def treino_listar():
        return Treinos.listar()
    @staticmethod
    def atleta_mais_rapido():
        treinos = Treinos.listar()
        menor = treinos[0]
        for treino in treinos: 
            if treino.pace() < menor.pace(): menor = treino
        return menor.get_id_atleta()    
    def treino_mais_rapido(id_atleta):
        treinos = Treinos.listar()
        for treino in treinos:
            if treino.get_id_atleta() == id_atleta: 
                menor = treino
                break
        for treino in treinos: 
            if treino.get_id_atleta() == id_atleta: 
                if treino.pace() < menor.pace(): menor = treino
        return menor


        
        
