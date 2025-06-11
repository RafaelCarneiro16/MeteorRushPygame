import pygame

class Vidas(pygame.sprite.Sprite):
    def __init__(self, grupo, posx = int):
        super().__init__(grupo)
        self.__imagem = pygame.image.load(rf'C:\GitHub\Jogo\imagens\coracao.png').convert_alpha()
        self.__image = pygame.transform.scale(self.__imagem, (50, 50))
        self.__rect = self.__image.get_rect(topright = (posx, 0))

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

    