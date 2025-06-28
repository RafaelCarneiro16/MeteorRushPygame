import pygame
from tela import Tela

class Explosao(pygame.sprite.Sprite):
    def __init__(self, group, tela: Tela, posicao):
        super().__init__(group)
        self.__tela = tela
        self.__sprites = pygame.image.load(r'C:\GitHub\Jogo\imagens\explosao.png').convert_alpha()
        self.__frames = []

        for i in range(4):
            frame = pygame.Surface((60, 60), pygame.SRCALPHA)
            frame.blit(self.__sprites, (0, 0), (i * 60, 0, 60, 60))
            self.__frames.append(frame)

        self.__indice = 0
        self.image = self.__frames[self.__indice]
        self.rect = self.image.get_rect(center=posicao)

        self.__tempo_animacao = 3
        self.__contador = 0

    # region Getters e Setters

    @property
    def tela(self):
        return self.__tela

    @tela.setter
    def tela(self, valor):
        self.__tela = valor

    @property
    def sprites(self):
        return self.__sprites

    @sprites.setter
    def sprites(self, valor):
        self.__sprites = valor

    @property
    def frames(self):
        return self.__frames

    @frames.setter
    def frames(self, valor):
        self.__frames = valor

    @property
    def indice(self):
        return self.__indice

    @indice.setter
    def indice(self, valor):
        self.__indice = valor

    @property
    def tempo_animacao(self):
        return self.__tempo_animacao

    @tempo_animacao.setter
    def tempo_animacao(self, valor):
        self.__tempo_animacao = valor

    @property
    def contador(self):
        return self.__contador

    @contador.setter
    def contador(self, valor):
        self.__contador = valor

    # endregion

    def update(self):
        self.contador += 1
        if self.contador >= self.tempo_animacao:
            self.contador = 0
            self.indice += 1

            if self.indice >= len(self.frames):
                self.kill()  
            else:
                self.image = self.frames[self.indice]
