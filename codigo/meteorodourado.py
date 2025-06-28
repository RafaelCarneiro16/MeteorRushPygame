import pygame 
import random
from tela import Tela

class Meteoro_Dourado(pygame.sprite.Sprite):
    def __init__(self, grupo, tela: Tela, jogador):
        super().__init__(grupo)
        self.__tela = tela
        self.__jogador = jogador
        try:
            self.__image = pygame.image.load(r'C:\GitHub\Jogo\imagens\meteoro_dourado.png').convert_alpha()
        except pygame.error as erro:
            print(f"⚠️ [METEORO_DOURADO] Falha ao carregar imagem do meteoro dourado: {erro}")
            self.__image = pygame.Surface((40, 40), pygame.SRCALPHA)
        self.__rect = self.__image.get_rect()
        self.__rect.center = (random.randint(0, tela.largura), -50)
        self.__pos = pygame.Vector2(self.rect.center)
        self.__pontos = 500 
        self.__seguindo = True

    #region Setters e Getters

    @property
    def tela(self):
        return self.__tela

    @tela.setter
    def tela(self, nova):
        self.__tela = nova

    @property
    def jogador(self):
        return self.__jogador

    @jogador.setter
    def jogador(self, novo):
        self.__jogador = novo

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
    def rect(self, novo):
        self.__rect = novo

    @property
    def pos(self):
        return self.__pos

    @pos.setter
    def pos(self, nova):
        self.__pos = nova

    @property
    def pontos(self):
        return self.__pontos

    @pontos.setter
    def pontos(self, valor):
        self.__pontos = valor

    @property
    def seguindo(self):
        return self.__seguindo

    @seguindo.setter
    def seguindo(self, valor):
        self.__seguindo = valor

    #endregion
    
    def update(self):
        if self.seguindo:
            destino = pygame.Vector2(self.jogador.rect.center)
            direcao = destino - self.pos

            if self.pos.y >= self.jogador.rect.centery:
                self.seguindo = False

            if direcao.length() != 0:
                direcao = direcao.normalize()

            self.pos += direcao * 4
            self.rect.center = self.pos
        else:
            self.rect.y += 4
            if self.rect.top > 600:
                self.kill()
