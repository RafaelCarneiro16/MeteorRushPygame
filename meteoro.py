import pygame
import random
from tela import Tela

class Meteoro(pygame.sprite.Sprite):
    def __init__(self, x, grupo):
        super().__init__(grupo)
        self.__image = pygame.image.load(rf"C:\jogotrab\imagens\meteoro.png").convert_alpha()
        self.__rect = self.__image.get_rect(center = (x, -50))
        self.__direcao = random.randint(-2,2)
    
    @property
    def image(self):
        return self.__image
    
    @image.setter
    def image(self, nova):
        self.__image = nova

    @property
    def rect(self):
        return self.__rect
    
    @rect.setter
    def rect(self, nova):
        self.__rect = nova

    def update(self):
        self.__rect.x += self.__direcao
        self.__rect.y += 4
        if self.__rect.top > 600 or self.__rect.left > 800 or self.__rect.right < 0 :
            self.kill()
          
         