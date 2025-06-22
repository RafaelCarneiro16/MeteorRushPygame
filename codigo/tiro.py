import pygame
from tela import Tela
from jogador import Jogador

class Tiro(pygame.sprite.Sprite):
    def __init__(self, posição : tuple, grupo, direcao):
        super().__init__(grupo)
        self.__image = pygame.image.load(rf"C:\GitHub\Jogo\imagens\tiro_jogador.png").convert_alpha()
        self.__rect = self.__image.get_rect(center = (posição))
        self.__direcao = direcao
        
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
    
    @property
    def direcao(self):
        return self.__direcao
    
    @direcao.setter
    def direcao(self, novo):
        self.__direcao = novo


    def draw(self, tela: Tela):
        tela.display.blit(self.__image, self.__rect)

    def update(self):
        self.__rect.y -= self.direcao * 10
        if self.__rect.bottom < 0:
           self.kill()

              