import json
import os
import pygame
from jogador_ranking import JogadorRanking

class GerenciadorRanking:
    def __init__(self):
        self.__jogadores = []
    
    @property
    def jogadores(self):
        return self.__jogadores
    
    @jogadores.setter
    def jogadores(self, valor):
        self.__jogadores = valor

    def adicionar_jogador(self, jogador: JogadorRanking):
        self.jogadores.append(jogador)
        self._ordenar_e_limitar()

    def _ordenar_e_limitar(self):
        self.jogadores.sort(key=lambda x: x.pontuacao, reverse=True)
        self.jogadores = self.jogadores[:10]

    def exibir_ranking_terminal(self):
        for i, jogador in enumerate(self.jogadores, 1):
            print(f"{i}. {jogador}")

    def salvar_em_arquivo(self, nome_arquivo: str):
        caminho = os.path.join(os.path.dirname(__file__), nome_arquivo)
        with open(caminho, "w") as f:
            json.dump([j.to_dict() for j in self.jogadores], f, indent=4)

    def carregar_de_arquivo(self, nome_arquivo: str):
        caminho = os.path.join(os.path.dirname(__file__), nome_arquivo)
        try:
            with open(caminho, "r") as f:
                dados = json.load(f)
                self.jogadores = [JogadorRanking.from_dict(d) for d in dados]
                self._ordenar_e_limitar()
        except FileNotFoundError:
            print("Arquivo não encontrado. Criando novo ranking vazio.")
            self.jogadores = []
        except json.JSONDecodeError:
            print("Erro ao ler o arquivo JSON. Ranking resetado.")
            self.jogadores = []

    def solicitar_nome(self, tela, clock) -> str:
        nome = ""
        fonte = pygame.font.Font(r"C:\GitHub\Jogo\fonte.ttf", 32)
        rodando = True

        while rodando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN and nome.strip() != "":
                        rodando = False
                    elif evento.key == pygame.K_BACKSPACE:
                        nome = nome[:-1]
                    else:
                        if len(nome) < 15 and evento.unicode.isprintable():
                            nome += evento.unicode

            tela.display.blit(tela.imagem_fundo, tela.rect_fundo)

            titulo = fonte.render("Digite seu nome e pressione Enter:", True, (255, 255, 255))
            campo = fonte.render(nome + "|", True, (255, 255, 0))

            tela.display.blit(titulo, (tela.largura // 2 - titulo.get_width() // 2, 200))
            tela.display.blit(campo, (tela.largura // 2 - campo.get_width() // 2, 260))

            pygame.display.update()
            clock.tick(60)

        return nome
