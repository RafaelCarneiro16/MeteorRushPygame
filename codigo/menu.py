import pygame
from tela import Tela
from jogo import Jogo
from botao import Botao


class Menu():
    def __init__(self, jogo: Jogo, tela: Tela, grupo_botoes: pygame.sprite.Group):
        self.__clock = pygame.time.Clock()
        self.__tela = tela  
        self.__jogo = jogo
        self.__grupo_botoes = grupo_botoes
        self.__logo_jogo = pygame.image.load('C:\GitHub\Jogo\imagens\icone_nome_jogo.png').convert_alpha()
        self.__logo_rect = self.__logo_jogo.get_rect(center = (400, 125))

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
    def texto(self):
        return self.__texto

    @texto.setter
    def texto(self, novo):
        self.__texto = novo    

    def desenha_menu(self):
        self.tela.display.blit(self.tela.imagem_fundo, self.tela.rect_fundo)


    def rodando_menu(self):
        botao_novojogo = Botao(self.__grupo_botoes, 'C:/GitHub/Jogo/imagens/bt_novo_jogo.png' , (400, 200))
        botao_continuar = None
        botao_ranking = Botao(self.__grupo_botoes, 'C:/GitHub/Jogo/imagens/bt_ranking.png', (400, 320))
        botao_som =  Botao(self.__grupo_botoes, 'C:/GitHub/Jogo/imagens/bt_som.png', (400, 442))

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
                   self.__jogo.novo_jogo()
                   rodando_menu = False
        
            pygame.display.update()
            self.clock.tick(60)
