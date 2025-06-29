import pygame 
import random
from tela import Tela

class Meteoro(pygame.sprite.Sprite):
    def __init__(self, x, grupo):
        super().__init__(grupo)
        self.__original_image = pygame.image.load(rf"C:\GitHub\Jogo\imagens\meteoro2.png").convert_alpha()
        self.__tamanho_imagem = random.uniform(0.8, 1.3) 
        self.__image = pygame.transform.rotozoom(self.original_image, random.randint(0, 360), self.tamanho_imagem)
        self.__rect = self.__image.get_rect(center = (x, -50))
        self.__direcao = random.randint(-2,2)
        self.__pontos = 0

        #region Pontuação 
        if self.tamanho_imagem < 0.95:
            self.pontos = 100  
        elif self.tamanho_imagem < 1.15:
            self.pontos = 50 
        else:
            self.pontos = 20 
        #endregion
      
    #region Setters e Getters
    @property
    def original_image(self):
        return self.__original_image
    
    @original_image.setter
    def original_image(self, nova):
        self.__original_image = nova

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

    @property
    def direcao(self):
        return self.__direcao
    
    @direcao.setter
    def direcao(self, valor):
        self.__direcao = valor
    
    @property
    def tamanho_imagem(self):
        return self.__tamanho_imagem
    
    @tamanho_imagem.setter
    def tamanho_imagem(self, valor):
        self.__tamanho_imagem = valor
    #endregion

    def update(self):
        self.rect.x += self.direcao
        self.rect.y += 4
        if self.rect.top > 600 or self.rect.left > 800 or self.rect.right < 0 :
            self.kill()

    
          
         