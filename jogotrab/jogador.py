import pygame
from tela import Tela

class Jogador(pygame.sprite.Sprite):
    def __init__(self, group, tela : Tela):
        super().__init__(group)
        self.__image = pygame.image.load(rf"C:\jogotrab\imagens\nave.gif").convert_alpha()
        self.__rect = self.__image.get_frect(center = (tela.largura/2, tela.altura/2))

    @property
    def image(self):
        return self.__image
    
    @image.setter
    def image(self, novo):
        self.__image = novo

    @property
    def rect(self):
        return self.__rect
    
    @rect.setter
    def rect(self, novo):
        self.__rect = novo
    
    def update(self, tela : Tela):
      tecla = pygame.key.get_pressed()

      if tecla[pygame.K_RIGHT] or tecla[pygame.K_d]:
        if self.__rect.right < tela.largura:
           self.__rect.right += 5

      if tecla[pygame.K_LEFT] or tecla[pygame.K_a]:
        if self.__rect.left > 0:
           self.__rect.left -= 5
    
      if tecla[pygame.K_UP] or tecla[pygame.K_w]:
        if self.__rect.top > 0 :
           self.__rect.top -= 3

      if tecla[pygame.K_DOWN] or tecla[pygame.K_s]:
        if self.__rect.bottom < tela.altura:
           self.__rect.bottom += 5
      