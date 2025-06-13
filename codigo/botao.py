import pygame

class Botao(pygame.sprite.Sprite):
    def __init__(self, grupo, caminho_imagem, posicao : tuple):
        super().__init__(grupo)
        self.__image = pygame.image.load(rf'{caminho_imagem}').convert_alpha()
        self.__rect = self.__image.get_rect(center = (posicao))

    @property
    def image(self):
        return self.__image
    
    @image.setter
    def image(self, nova_imagem):
        self.__image =  nova_imagem

    @property
    def rect(self):
        return self.__rect
    
    @rect.setter
    def rect(self, novo):
        self.__rect =  novo
    @property
    def posicao(self):
        return self.__posicao
    
    @posicao.setter
    def posicao(self, nova_posicao):
        self.__posicao =  nova_posicao

        return False

