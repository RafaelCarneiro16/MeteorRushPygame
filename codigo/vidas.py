import pygame

class Vidas(pygame.sprite.Sprite):
    def __init__(self, grupo, posx = int):
        super().__init__(grupo)
        self.__imagem_vida = pygame.image.load(rf'C:\GitHub\Jogo\imagens\vida.png').convert_alpha()
        self.__imagem_vida = pygame.transform.scale(self.__imagem_vida, (50, 50))
        self.__imagem_vidaperdida = pygame.image.load(rf'C:\GitHub\Jogo\imagens\vida_perdida.png').convert_alpha()
        self.__imagem_vidaperdida = pygame.transform.scale(self.__imagem_vidaperdida, (50, 50))
        self.__image = self.__imagem_vida
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

    def perder_vida(self):
        self.image = self.__imagem_vidaperdida
    
        
    

    