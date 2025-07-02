import json
import os
import pygame
from jogador_ranking import JogadorRanking
from botao import Botao

class GerenciadorRanking:
    def __init__(self):
        self.__jogadores = []

    # region Setters e Getters
    @property
    def jogadores(self):
        return self.__jogadores

    @jogadores.setter
    def jogadores(self, valor):
        self.__jogadores = valor
    # endregion

    def adicionar_jogador(self, jogador: JogadorRanking):
        try:
            self.jogadores.append(jogador)
            self._ordenar_e_limitar()
        except Exception as erro:
            print(f"⚠️ [RANKING] Erro ao adicionar jogador: {erro}")

    def _ordenar_e_limitar(self):
        try:
            self.jogadores.sort(key=lambda x: x.pontuacao, reverse=True)
            self.jogadores = self.jogadores[:10]
        except Exception as erro:
            print(f"⚠️ [RANKING] Erro ao ordenar e limitar ranking: {erro}")

    def exibir_ranking_terminal(self):
        try:
            for i, jogador in enumerate(self.jogadores, 1):
                print(f"{i}. {jogador}")
        except Exception as erro:
            print(f"⚠️ [RANKING] Erro ao exibir ranking no terminal: {erro}")

    def salvar_em_arquivo(self, nome_arquivo: str):
        try:
            caminho = os.path.join(os.path.dirname(__file__), nome_arquivo)
            with open(caminho, "w") as f:
                json.dump([j.to_dict() for j in self.jogadores], f, indent=4)
            print(f"✅ [RANKING] Ranking salvo com sucesso no arquivo: {nome_arquivo}")
        except Exception as erro:
            print(f"⚠️ [RANKING] Erro ao salvar o arquivo {nome_arquivo}: {erro}")

    def carregar_de_arquivo(self, nome_arquivo: str):
        try:
            caminho = os.path.join(os.path.dirname(__file__), nome_arquivo)
            with open(caminho, "r") as f:
                dados = json.load(f)
                self.jogadores = [JogadorRanking.from_dict(d) for d in dados]
                self._ordenar_e_limitar()
            print(f"✅ [RANKING] Ranking carregado com sucesso do arquivo: {nome_arquivo}")
        except FileNotFoundError:
            print(f"⚠️ [RANKING] Arquivo {nome_arquivo} não encontrado. Criando novo ranking vazio.")
            self.jogadores = []
        except json.JSONDecodeError:
            print(f"⚠️ [RANKING] Erro ao ler o arquivo JSON {nome_arquivo}. Ranking resetado.")
            self.jogadores = []
        except Exception as erro:
            print(f"⚠️ [RANKING] Erro inesperado ao carregar o arquivo {nome_arquivo}: {erro}")
            self.jogadores = []

    def solicitar_nome(self, tela, clock, botao: Botao) -> str:
        nome = ""
        fonte = pygame.font.Font(os.path.join('fonte.ttf'), 32)
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

            try:
                tela.display.blit(tela.imagem_fundo, tela.rect_fundo)
                tela.display.blit(botao.image, botao.rect)

                titulo = fonte.render("Digite seu nome e pressione Enter:", True, (255, 255, 255))
                campo = fonte.render(nome + "|", True, (255, 255, 0))

                tela.display.blit(titulo, (tela.largura // 2 - titulo.get_width() // 2, 200))
                tela.display.blit(campo, (tela.largura // 2 - campo.get_width() // 2, 260))

                pygame.display.update()
                clock.tick(60)
            except Exception as erro:
                print(f"⚠️ [RANKING] Erro na tela de solicitação de nome: {erro}")

        return nome

    def exibir_ranking(self, tela, clock):
        rodando = True
        fonte = pygame.font.Font(os.path.join('fonte.ttf'), 32)

        while rodando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                    rodando = False

            try:
                tela.display.blit(tela.imagem_fundo, tela.rect_fundo)

                titulo = fonte.render("Ranking de Pontuação", True, (255, 255, 255))
                tela.display.blit(titulo, (tela.largura // 2 - titulo.get_width() // 2, 50))

                for i, jogador in enumerate(self.jogadores, 1):
                    texto = fonte.render(f"{i}. {jogador.nome}: {jogador.pontuacao} pts", True, (255, 255, 255))
                    tela.display.blit(texto, (150, 100 + i * 40))

                pygame.display.update()
                clock.tick(60)
            except Exception as erro:
                print(f"⚠️ [RANKING] Erro na exibição do ranking: {erro}")
