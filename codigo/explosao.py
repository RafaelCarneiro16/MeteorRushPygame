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

    def update(self):
        self.__contador += 1
        if self.__contador >= self.__tempo_animacao:
            self.__contador = 0
            self.__indice += 1

            if self.__indice >= len(self.__frames):
                self.kill() 
            else:
                self.image = self.__frames[self.__indice]