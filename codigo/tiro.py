import pygame
import os

class Tiro(pygame.sprite.Sprite):
    def __init__(self, posição : tuple, grupo, direcao, imagem = None):
        super().__init__(grupo)

        if imagem is None:
            imagem = os.path.join('imagens', 'tiro_jogador.png')

        self.__image = pygame.image.load(os.path.join('imagens', f'{imagem}')).convert_alpha()
        self.__rect = self.image.get_rect(center = (posição))
        self.__direcao = direcao

    #region Setters e Getters
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
        
    def update(self):
        self.rect.y -= self.direcao * 10
        if self.rect.bottom < 0:
           self.kill()
    
    #endregion