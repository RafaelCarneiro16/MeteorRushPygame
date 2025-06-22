class JogadorRanking:
    def __init__(self, nome: str, pontuacao: int):
        self.__nome = nome
        self.__pontuacao = pontuacao
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def pontuacao(self):
        return self.__pontuacao

    @pontuacao.setter
    def pontuacao(self, value):
        self.__pontuacao = value

    def to_dict(self):
        return {"nome": self.nome, "pontuacao": self.pontuacao}

    @staticmethod
    def from_dict(data):
        return JogadorRanking(data["nome"], data["pontuacao"])

    def __repr__(self):
        return f"{self.nome}: {self.pontuacao} pts"