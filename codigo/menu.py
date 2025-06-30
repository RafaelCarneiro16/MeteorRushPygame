import pygame
import json
from tela import Tela
from jogo import Jogo
from botao import Botao
from som import Som
from texto import Texto
from jogador_ranking import JogadorRanking
from gerenciador_raking import GerenciadorRanking
from gerenciador_progresso import GerenciadorProgresso
from vidas import Vidas
import os

class Menu():
    def __init__(self, jogo: Jogo):
        self.__clock = pygame.time.Clock()
        self.__tela = Tela(800, 600, 'fundo2.png')
        self.__jogo = jogo
        self.__grupo_botoes = pygame.sprite.Group()
        self.__gerenciador_progresso = GerenciadorProgresso()
        try:
            self.__logo_jogo = pygame.image.load(os.path.join('imagens', 'icone_nome_jogo.png')).convert_alpha()
        except pygame.error as erro:
            print(f"⚠️ [MENU] Falha ao carregar a imagem do logo: {erro}")
            self.__logo_jogo = pygame.Surface((200, 100), pygame.SRCALPHA)
        self.__logo_rect = self.logo_jogo.get_rect(center = (400, 125))
        self.__som = Som()
        self.__ranking = GerenciadorRanking()
        self.__ranking.carregar_de_arquivo("ranking.json")

        try:
            self.__fonte = pygame.font.Font(os.path.join('fonte.ttf'), 24)
        except pygame.error as erro:
            print(f"⚠️ [MENU] Falha ao carregar fonte: {erro}")
            self.__fonte = pygame.font.SysFont(None, 24)
            
        self.__texto_titulo = Texto(48, "Gerenciador de Som", (255,255,255), (self.tela.largura // 2, 50), self.tela)
        self.__texto_instrucao = Texto(24, "Pressione ESC para voltar ao menu principal", (255,255,255), (self.tela.largura // 2, self.tela.altura - 30), self.tela)

    # region Getters e Setters
    @property
    def clock(self):
        return self.__clock

    @clock.setter
    def clock(self, value):
        self.__clock = value

    @property
    def tela(self):
        return self.__tela

    @tela.setter
    def tela(self, value):
        self.__tela = value

    @property
    def jogo(self):
        return self.__jogo

    @jogo.setter
    def jogo(self, value):
        self.__jogo = value

    @property
    def grupo_botoes(self):
        return self.__grupo_botoes

    @grupo_botoes.setter
    def grupo_botoes(self, value):
        self.__grupo_botoes = value

    @property
    def logo_jogo(self):
        return self.__logo_jogo

    @logo_jogo.setter
    def logo_jogo(self, value):
        self.__logo_jogo = value

    @property
    def logo_rect(self):
        return self.__logo_rect

    @logo_rect.setter
    def logo_rect(self, value):
        self.__logo_rect = value

    @property
    def som(self):
        return self.__som

    @som.setter
    def som(self, value):
        self.__som = value

    @property
    def ranking(self):
        return self.__ranking

    @ranking.setter
    def ranking(self, value):
        self.__ranking = value

    @property
    def fonte(self):
        return self.__fonte

    @fonte.setter
    def fonte(self, value):
        self.__fonte = value

    @property
    def texto_titulo(self):
        return self.__texto_titulo

    @texto_titulo.setter
    def texto_titulo(self, value):
        self.__texto_titulo = value

    @property
    def texto_instrucao(self):
        return self.__texto_instrucao

    @texto_instrucao.setter
    def texto_instrucao(self, value):
        self.__texto_instrucao = value

    @property
    def gerenciador_progresso(self):
        return self.__gerenciador_progresso
    
    @gerenciador_progresso.setter
    def gerenciador_progresso(self, valor):
        self.__gerenciador_progresso = valor

    # endregion

    def desenha_menu(self):
        self.tela.display.blit(self.tela.imagem_fundo, self.tela.rect_fundo)

    def menu_volume(self):
        self.som.exibir_menu_volume(self.tela, self.clock, self.texto_titulo, self.texto_instrucao)

    def exibir_ranking(self):
        self.ranking.exibir_ranking(self.tela, self.clock)

    def rodando_menu(self):
        botao_continuar = Botao(self.grupo_botoes, 'bt_continuar.png', (400,175))
        botao_novojogo = Botao(self.grupo_botoes, 'bt_novo_jogo.png', (400,295))
        botao_ranking = Botao(self.grupo_botoes, 'bt_ranking.png', (400,413))
        botao_som = Botao(self.grupo_botoes, 'bt_som.png', (400,532))

        self.som.tocar_musica('musica_menu.wav')

        rodando_menu = True

        while rodando_menu:
            mouse_pos = pygame.mouse.get_pos()
            mouse_botao = pygame.mouse.get_pressed()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.desenha_menu()
            self.tela.display.blit(self.logo_jogo, self.logo_rect)
            self.grupo_botoes.update()
            self.grupo_botoes.draw(self.tela.display)

            if mouse_botao[0]:
                if botao_novojogo.rect.collidepoint(mouse_pos):
                    self.som.tocar_efeitos("clique_inicio.wav")
                    self.som.parar_musica()
                    self.jogo.novo_jogo()
                    rodando_menu = False

                if botao_som.rect.collidepoint(mouse_pos):
                    self.som.tocar_efeitos("clique.mp3")
                    self.menu_volume()
                    rodando_menu = False

                if botao_ranking.rect.collidepoint(mouse_pos):
                    self.som.tocar_efeitos("clique.mp3")
                    self.exibir_ranking()

                if botao_continuar.rect.collidepoint(mouse_pos):
                    self.som.tocar_efeitos("clique_inicio.wav")
                    progresso = self.gerenciador_progresso.carregar_progresso()
                    
                    if progresso:
                        self.som.parar_musica()
                        self.jogo.novo_jogo(
                            pontuacao=progresso.get("pontuacao", 0),
                            vidas=progresso.get("vidas", 3)
                        )
                        rodando_menu = False
                    else:
                        print("⚠️ Nenhum progresso para continuar.")

            pygame.display.update()
            self.clock.tick(60)
