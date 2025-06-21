import pygame
from tela import Tela

class Texto:
    def __init__(self, tamanho: int, texto: str, cor: tuple, posicao: tuple, tela: Tela):
        self.__tamanho = tamanho
        self.__cor = cor
        self.__texto_str = texto
        self.__tela = tela
        self.__fonte = pygame.font.Font(r'C:\GitHub\Jogo\fonte.ttf', self.__tamanho)
        self.__texto = self.__fonte.render(self.__texto_str, True, self.__cor)
        self.__rect = self.__texto.get_rect(center= posicao)

    #region Setters e Getters
    @property
    def tamanho(self):
        return self.__tamanho

    @tamanho.setter
    def tamanho(self, value):
        self.__tamanho = value

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, value):
        self.__cor = value

    @property
    def texto_str(self):
        return self.__texto_str

    @texto_str.setter
    def texto_str(self, value):
        self.__texto_str = value

    @property
    def tela(self):
        return self.__tela

    @tela.setter
    def tela(self, value):
        self.__tela = value

    @property
    def fonte(self):
        return self.__fonte

    @fonte.setter
    def fonte(self, value):
        self.__fonte = value

    @property
    def texto(self):
        return self.__texto

    @texto.setter
    def texto(self, value):
        self.__texto = value

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, value):
        self.__rect = value

    #endregion    

    def desenha_texto(self):
        self.__tela.display.blit(self.__texto, self.__rect)
