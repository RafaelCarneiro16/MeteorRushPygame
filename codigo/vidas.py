import pygame
import os

class Vidas(pygame.sprite.Sprite):
    def __init__(self, grupo, posx=int):
        super().__init__(grupo)
        try:
            self.__imagem_vida = pygame.image.load(os.path.join('imagens', 'vida.png')).convert_alpha()
            self.__imagem_vida = pygame.transform.scale(self.imagem_vida, (50, 50))
        except pygame.error as erro:
            print(f"⚠️ [VIDAS] Falha ao carregar a imagem de vida: {erro}")

        self.__image = self.imagem_vida
        self.__rect = self.image.get_rect(topright=(posx, 0))

    # region Setters e Getters
    @property
    def imagem_vida(self):
        return self.__imagem_vida
    
    @imagem_vida.setter
    def imagem_vida(self, novo):
        self.__imagem_vida = novo

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
    # endregion
