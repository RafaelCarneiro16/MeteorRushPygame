import pygame
import os

class Botao(pygame.sprite.Sprite):
    def __init__(self, grupo, imagem, posicao: tuple):
        super().__init__(grupo)
        try:
            self.__posicao = posicao
            try:
                self.__image = pygame.image.load(os.path.join('imagens', f'{imagem}')).convert_alpha()
            except pygame.error as erro_img:
                print(f"⚠️ [BOTAO] Erro ao carregar imagem: {erro_img}")
                self.__image = None
            if self.__image:
                self.__rect = self.__image.get_rect(center=self.posicao)
            else:
                self.__rect = pygame.Rect(self.posicao[0], self.posicao[1], 0, 0)
        except Exception as erro:
            print(f"⚠️ [BOTAO] Erro no construtor: {erro}")

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
    def posicao(self):
        return self.__posicao
    
    @posicao.setter
    def posicao(self, nova_posicao):
        self.__posicao = nova_posicao

    #endregion
