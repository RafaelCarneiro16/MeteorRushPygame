
class JogadorRanking:
    def __init__(self, nome: str, pontuacao: int):
        self.nome = nome
        self.pontuacao = pontuacao

    def to_dict(self):
        return {"nome": self.nome, "pontuacao": self.pontuacao}

    @staticmethod
    def from_dict(data):
        return JogadorRanking(data["nome"], data["pontuacao"])

    def __repr__(self):
        return f"{self.nome}: {self.pontuacao} pts"