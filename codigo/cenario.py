import pygame
from tela import Tela

class Cenario(pygame.sprite.Group):
    def __init__(self, tela: Tela):
        super().__init__()
        self.__tela = tela

        self.__imagem_planeta = pygame.image.load(r"C:\GitHub\Jogo\imagens\planeta.png").convert_alpha()
        self.__imagem_sol = pygame.image.load(r"C:\GitHub\Jogo\imagens\sol.png").convert_alpha()

        self.__sprite = pygame.sprite.Sprite()
        self.__sprite.image = self.__imagem_planeta
        self.__sprite.rect = self.__sprite.image.get_rect(topleft=(-999, -999))  # Fora da tela (Não aparecer)
        self.add(self.__sprite)

        self.__mostrando = False
        self.__modo_atual = "planeta"
        self.__proximo_evento = pygame.time.get_ticks() + 5000  # Tempo entre o sol e o planeta

    # region Getters e Setters

    @property
    def tela(self):
        return self.__tela
    
    @tela.setter
    def tela(self, value):
        self.__tela = value

    @property
    def imagem_planeta(self):
        return self.__imagem_planeta

    @imagem_planeta.setter
    def imagem_planeta(self, nova):
        self.__imagem_planeta = nova

    @property
    def imagem_sol(self):
        return self.__imagem_sol

    @imagem_sol.setter
    def imagem_sol(self, nova):
        self.__imagem_sol = nova

    @property
    def sprite(self):
        return self.__sprite

    @sprite.setter
    def sprite(self, novo_sprite):
        self.__sprite = novo_sprite

    @property
    def mostrando(self):
        return self.__mostrando

    @mostrando.setter
    def mostrando(self, status):
        self.__mostrando = status

    @property
    def modo_atual(self):
        return self.__modo_atual

    @modo_atual.setter
    def modo_atual(self, modo):
        self.__modo_atual = modo

    @property
    def proximo_evento(self):
        return self.__proximo_evento

    @proximo_evento.setter
    def proximo_evento(self, tempo):
        self.__proximo_evento = tempo

    # endregion

    def update(self):
        agora = pygame.time.get_ticks()

        if not self.__mostrando:
            if agora >= self.proximo_evento:
                if self.modo_atual == "planeta":
                    self.sprite.image = self.imagem_planeta
                    self.__sprite.rect = self.__sprite.image.get_rect(topleft=(-100, -self.sprite.image.get_height()))
                    self.__modo_atual = "sol"
                else:
                    self.__sprite.image = self.__imagem_sol
                    self.__sprite.rect = self.__sprite.image.get_rect(topleft=(680, -self.sprite.image.get_height()))
                    self.__modo_atual = "planeta"

                self.__mostrando = True
        else:
            self.__sprite.rect.y += 1
            if self.__sprite.rect.top > self.tela.altura:
                self.__sprite.rect.topleft = (-999, -999)
                self.__mostrando = False
                self.__proximo_evento = agora + 5000
