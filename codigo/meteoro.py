import pygame 
import random
from tela import Tela

class Meteoro(pygame.sprite.Sprite):
    def __init__(self, x, grupo):
        super().__init__(grupo)
        self.original_image = pygame.image.load(rf"C:\MeusGits\MeteorRushPyGame\imagens\meteoro.png").convert_alpha()
        tamanho_imagem = random.uniform(0.8, 1.3) 
        self.__image = pygame.transform.rotozoom(self.original_image, random.randint(0, 360), tamanho_imagem)
        self.__rect = self.__image.get_rect(center = (x, -50))
        self.__direcao = random.randint(-2,2)
      
        # Pontuação temporária
        if tamanho_imagem < 0.95:
            self.__pontos = 100  
        elif tamanho_imagem < 1.15:
            self.__pontos = 50 
        else:
            self.__pontos = 20 
    
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

    @property
    def pontos(self):
        return self.__pontos
    
    @pontos.setter
    def pontos(self, nova):
        self.__pontos = nova

    def update(self):
        self.__rect.x += self.__direcao
        self.__rect.y += 4
        if self.__rect.top > 600 or self.__rect.left > 800 or self.__rect.right < 0 :
            self.kill()
          
         