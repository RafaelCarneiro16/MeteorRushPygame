import pygame
from tela import Tela
from jogador import Jogador

class Tiro(pygame.sprite.Sprite):
    def __init__(self, posição : tuple, grupo):
        super().__init__(grupo)
        self.__image = pygame.image.load(rf"C:\jogotrab\imagens\laser.png").convert_alpha()
        self.__rect = self.__image.get_rect(center = (posição))
        
    @property
    def image(self):
        return self.__image
    
    @image.setter
    def image(self, nova_imagem):
        self.__image = nova_imagem 

    @property
    def rect(self):
        return self.__rect
    
    @rect.setter
    def rect(self, novo):
        self.__rect = novo

    def draw(self, tela: Tela):
        tela.display.blit(self.__image, self.__rect)

    def update(self):
        self.__rect.y -= 10 
        if self.__rect.bottom < 0:
           self.kill()

              