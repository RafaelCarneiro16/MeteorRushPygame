import pygame
import json
from tela import Tela
from jogo import Jogo
from botao import Botao
from som import Som
from texto import Texto
from jogador_ranking import JogadorRanking
from gerenciador_raking import GerenciadorRanking

class Menu():
    def __init__(self, jogo: Jogo, tela: Tela, som: Som, ranking: GerenciadorRanking):
        self.__clock = pygame.time.Clock()
        self.__tela = tela  
        self.__jogo = jogo
        self.__grupo_botoes = pygame.sprite.Group()
        self.__logo_jogo = pygame.image.load('C:/GitHub/Jogo/imagens/icone_nome_jogo.png').convert_alpha()
        self.__logo_rect = self.__logo_jogo.get_rect(center = (400, 125))
        self.__som = som
        self.__ranking = ranking
        self.__fonte = pygame.font.Font(rf'C:\GitHub\Jogo\fonte.ttf', 24)
        self.__texto_titulo = Texto(48, "Gerenciador de Som", (255,255,255), (self.__tela.largura // 2, 50), self.__tela)
        self.__texto_instrucao = Texto(24, "Pressione ESC para voltar ao menu principal", (255,255,255), (self.__tela.largura // 2, self.__tela.altura - 30), self.__tela)

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
    # endregion

    def desenha_menu(self):
        self.tela.display.blit(self.tela.imagem_fundo, self.tela.rect_fundo)

    def menu_volume(self):
        rodando = True

        while rodando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                    rodando = False
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    if self.som.cursor_musica.collidepoint(pygame.mouse.get_pos()):
                        self.som.arrastando_musica = True
                    if self.som.cursor_efeitos.collidepoint(pygame.mouse.get_pos()):
                        self.som.arrastando_efeitos = True
                elif evento.type == pygame.MOUSEBUTTONUP:
                    self.som.arrastando_musica = False
                    self.som.arrastando_efeitos = False

            mouse_x = pygame.mouse.get_pos()[0]

            if self.som.arrastando_musica:
                self.som.cursor_musica.centerx = max(
                    self.som.x_barra_volume,
                    min(mouse_x, self.som.x_barra_volume + self.som.largura_barra_volume)
                )
                novo_volume = (self.__som.cursor_musica.centerx - self.som.x_barra_volume) / self.som.largura_barra_volume
                self.som.volume_musica = novo_volume

            if self.som.arrastando_efeitos:
                self.som.cursor_efeitos.centerx = max(
                    self.som.x_barra_volume,
                    min(mouse_x, self.som.x_barra_volume + self.som.largura_barra_volume))
                novo_volume = (self.som.cursor_efeitos.centerx - self.som.x_barra_volume) / self.som.largura_barra_volume
                self.som.volume_efeitos = novo_volume
                self.som.atualizar_volumes()

            texto_musica = Texto(
                24,
                f'Música: {int(self.som.volume_musica * 100)}%',
                (255, 255, 255),
                (self.som.x_barra_volume + self.som.largura_barra_volume // 2, self.som.y_barra_musica - 20),
                self.tela)

            texto_efeitos = Texto(
                24,
                f'Efeitos: {int(self.som.volume_efeitos * 100)}%',
                (255, 255, 255),
                (self.som.x_barra_volume + self.som.largura_barra_volume // 2, self.som.y_barra_efeitos - 20),
                self.tela
            )

            self.tela.display.blit(self.tela.imagem_fundo, self.tela.rect_fundo)
            self.texto_instrucao.desenha_texto()
            self.texto_titulo.desenha_texto()

            pygame.draw.rect(self.tela.display, (200, 200, 200), (self.som.x_barra_volume, self.som.y_barra_musica, self.som.largura_barra_volume, self.som.altura_barra_volume))
            pygame.draw.rect(self.tela.display, (255, 255, 255), self.som.cursor_musica)

            pygame.draw.rect(self.tela.display, (200, 200, 200), (self.som.x_barra_volume, self.som.y_barra_efeitos, self.som.largura_barra_volume, self.som.altura_barra_volume))
            pygame.draw.rect(self.tela.display, (255, 255, 255), self.som.cursor_efeitos)

            texto_musica.desenha_texto()
            texto_efeitos.desenha_texto()

            pygame.display.flip()
            self.clock.tick(60)

    def exibir_ranking(self):
        rodando = True
        fonte = pygame.font.Font(r'C:\GitHub\Jogo\fonte.ttf', 32)

        while rodando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                    rodando = False

            self.tela.display.blit(self.tela.imagem_fundo, self.tela.rect_fundo)

            titulo = self.fonte.render("Ranking de Pontuação", True, (255, 255, 255))
            self.tela.display.blit(titulo, (self.tela.largura // 2 - titulo.get_width() // 2, 50))

            for i, jogador in enumerate(self.ranking.jogadores, 1):
                texto = fonte.render(f"{i}. {jogador.nome}: {jogador.pontuacao} pts", True, (255, 255, 255))
                self.tela.display.blit(texto, (150, 100 + i * 40))

            pygame.display.update()
            self.clock.tick(60)

    def rodando_menu(self):
        botao_continuar = Botao(self.grupo_botoes, r'C:\GitHub\Jogo\imagens\bt_continuar.png', (400,175))
        botao_novojogo = Botao(self.grupo_botoes, 'C:/GitHub/Jogo/imagens/bt_novo_jogo.png', (400,295))
        botao_ranking = Botao(self.grupo_botoes, 'C:/GitHub/Jogo/imagens/bt_ranking.png', (400,413))
        botao_som = Botao(self.grupo_botoes, 'C:/GitHub/Jogo/imagens/bt_som.png', (400,532))

        self.som.tocar_musica(r"C:\GitHub\Jogo\sons\musica_menu.wav")

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
                    self.som.tocar_efeitos(r"C:\GitHub\Jogo\sons\clique_inicio.wav")
                    self.som.parar_musica()
                    self.jogo.novo_jogo()
                    rodando_menu = False

                if botao_som.rect.collidepoint(mouse_pos):
                    self.som.tocar_efeitos(r"C:\GitHub\Jogo\sons\clique.mp3")
                    self.menu_volume()
                    rodando_menu = False

                if botao_ranking.rect.collidepoint(mouse_pos):
                    self.som.tocar_efeitos(r"C:\GitHub\Jogo\sons\clique.mp3")
                    self.exibir_ranking()

            pygame.display.update()
            self.clock.tick(60)
