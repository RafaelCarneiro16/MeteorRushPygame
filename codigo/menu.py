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
    def __init__(self, jogo: Jogo, tela: Tela, grupo_botoes: pygame.sprite.Group, som: Som, ranking: GerenciadorRanking):
        self.__clock = pygame.time.Clock()
        self.__tela = tela  
        self.__jogo = jogo
        self.__grupo_botoes = grupo_botoes
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
    def clock(self, novo):
        self.__clock = novo

    @property
    def tela(self):
        return self.__tela

    @tela.setter
    def tela(self, nova):
        self.__tela = nova

    @property
    def jogo(self):
        return self.__jogo

    @jogo.setter
    def jogo(self, novo):
        self.__jogo = novo

    @property
    def som(self):
        return self.__som
    
    @som.setter
    def som(self, valor):
        self.__som = valor
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
                    if self.__som.cursor_musica.collidepoint(pygame.mouse.get_pos()):
                        self.__som.arrastando_musica = True
                    if self.__som.cursor_efeitos.collidepoint(pygame.mouse.get_pos()):
                        self.__som.arrastando_efeitos = True
                elif evento.type == pygame.MOUSEBUTTONUP:
                    self.__som.arrastando_musica = False
                    self.__som.arrastando_efeitos = False

            mouse_x = pygame.mouse.get_pos()[0]

            if self.__som.arrastando_musica:
                self.__som.cursor_musica.centerx = max(
                    self.__som.x_barra_volume,
                    min(mouse_x, self.__som.x_barra_volume + self.__som.largura_barra_volume)
                )
                novo_volume = (self.__som.cursor_musica.centerx - self.__som.x_barra_volume) / self.__som.largura_barra_volume
                self.__som.volume_musica = novo_volume

            if self.__som.arrastando_efeitos:
                self.__som.cursor_efeitos.centerx = max(
                    self.__som.x_barra_volume,
                    min(mouse_x, self.__som.x_barra_volume + self.__som.largura_barra_volume)
                )
                novo_volume = (self.__som.cursor_efeitos.centerx - self.__som.x_barra_volume) / self.__som.largura_barra_volume
                self.__som.volume_efeitos = novo_volume
                self.__som.atualizar_volumes()

            texto_musica = Texto(
                24,
                f'Música: {int(self.__som.volume_musica * 100)}%',
                (255, 255, 255),
                (self.__som.x_barra_volume + self.__som.largura_barra_volume // 2, self.__som.y_barra_musica - 20),
                self.__tela
            )

            texto_efeitos = Texto(
                24,
                f'Efeitos: {int(self.__som.volume_efeitos * 100)}%',
                (255, 255, 255),
                (self.__som.x_barra_volume + self.__som.largura_barra_volume // 2, self.__som.y_barra_efeitos - 20),
                self.__tela
            )

            self.__tela.display.blit(self.__tela.imagem_fundo, self.__tela.rect_fundo)
            self.__texto_instrucao.desenha_texto()
            self.__texto_titulo.desenha_texto()

            pygame.draw.rect(self.__tela.display, (200, 200, 200), (self.__som.x_barra_volume, self.__som.y_barra_musica, self.__som.largura_barra_volume, self.__som.altura_barra_volume))
            pygame.draw.rect(self.__tela.display, (255, 255, 255), self.__som.cursor_musica)

            pygame.draw.rect(self.__tela.display, (200, 200, 200), (self.__som.x_barra_volume, self.__som.y_barra_efeitos, self.__som.largura_barra_volume, self.__som.altura_barra_volume))
            pygame.draw.rect(self.__tela.display, (255, 255, 255), self.__som.cursor_efeitos)

            texto_musica.desenha_texto()
            texto_efeitos.desenha_texto()

            pygame.display.flip()
            self.__clock.tick(60)

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

            self.__tela.display.blit(self.__tela.imagem_fundo, self.__tela.rect_fundo)

            titulo = self.__fonte.render("Ranking de Pontuação", True, (255, 255, 255))
            self.__tela.display.blit(titulo, (self.__tela.largura // 2 - titulo.get_width() // 2, 50))

            for i, jogador in enumerate(self.__ranking.jogadores, 1):
                texto = fonte.render(f"{i}. {jogador.nome}: {jogador.pontuacao} pts", True, (255, 255, 255))
                self.__tela.display.blit(texto, (150, 100 + i * 40))

            pygame.display.update()
            self.clock.tick(60)

    def rodando_menu(self):
        botao_novojogo = Botao(self.__grupo_botoes, 'C:/GitHub/Jogo/imagens/bt_novo_jogo.png', (400, 200))
        botao_continuar = None
        botao_ranking = Botao(self.__grupo_botoes, 'C:/GitHub/Jogo/imagens/bt_ranking.png', (400, 320))
        botao_som = Botao(self.__grupo_botoes, 'C:/GitHub/Jogo/imagens/bt_som.png', (400, 442))

        self.__som.tocar_musica(r"C:\GitHub\Jogo\sons\musica_menu.wav")

        rodando_menu = True

        while rodando_menu:
            mouse_pos = pygame.mouse.get_pos()
            mouse_botao = pygame.mouse.get_pressed()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.desenha_menu()
            self.__tela.display.blit(self.__logo_jogo, self.__logo_rect)
            self.__grupo_botoes.update()
            self.__grupo_botoes.draw(self.__tela.display)

            if mouse_botao[0]:
                if botao_novojogo.rect.collidepoint(mouse_pos):
                    self.__som.tocar_efeitos(r"C:\GitHub\Jogo\sons\clique_inicio.wav")
                    self.__som.parar_musica()
                    self.__jogo.novo_jogo()
                    rodando_menu = False

                if botao_som.rect.collidepoint(mouse_pos):
                    self.__som.tocar_efeitos(r"C:\GitHub\Jogo\sons\clique.mp3")
                    self.menu_volume()
                    rodando_menu = False

                if botao_ranking.rect.collidepoint(mouse_pos):
                    self.__som.tocar_efeitos(r"C:\GitHub\Jogo\sons\clique.mp3")
                    self.exibir_ranking()

            pygame.display.update()
            self.clock.tick(60)
