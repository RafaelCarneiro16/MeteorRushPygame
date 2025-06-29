import pygame
from tela import Tela
import os

class Jogador(pygame.sprite.Sprite):
    def __init__(self, group, tela: Tela):
        super().__init__(group)
        self.__tela = tela
        
        try:
            self.__frames = [
                pygame.image.load(os.path.join('imagens', 'nave0.png')).convert_alpha(),
                pygame.image.load(os.path.join('imagens', 'nave1.png')).convert_alpha(),
                pygame.image.load(os.path.join('imagens', 'nave2.png')).convert_alpha(),
                pygame.image.load(os.path.join('imagens', 'nave3.png')).convert_alpha(),
                pygame.image.load(os.path.join('imagens', 'nave4.png')).convert_alpha()
            ]
        except pygame.error as erro:
            print(f"⚠️ [JOGADOR] Falha ao carregar imagens dos frames da nave: {erro}")
            self.__frames = []
        
        self.__indice = 0
        if self.__frames:
            self.__image = self.frames[self.indice]
            self.__rect = self.image.get_rect(center=(400, 400))
        else:
            self.__image = None
            self.__rect = pygame.Rect(400, 400, 50, 50)  # fallback retângulo

        self.__tempo_animacao = 5
        self.__contador = 0

        try:
            self.__vento = pygame.image.load(os.path.join('imagens', 'vento.png')).convert_alpha()
            self.__vento_rect = self.vento.get_rect(center=self.rect.center)
        except pygame.error as erro:
            print(f"⚠️ [JOGADOR] Falha ao carregar imagem do vento: {erro}")
            self.__vento = None
            self.__vento_rect = pygame.Rect(0, 0, 0, 0)

        self.__subindo = False
        self.__tiro_triplo = False
  
    # region Getters e Setters
    @property
    def tela(self):
        return self.__tela

    @tela.setter
    def tela(self, value):
        self.__tela = value

    @property
    def frames(self):
        return self.__frames

    @frames.setter
    def frames(self, value):
        self.__frames = value

    @property
    def indice(self):
        return self.__indice

    @indice.setter
    def indice(self, value):
        self.__indice = value
    
    @property
    def image(self):
        return self.__image
    
    @image.setter
    def image(self, value):
        self.__image = value

    @property
    def rect(self):
        return self.__rect

    @rect.setter 
    def rect(self, value):
        self.__rect = value

    @property
    def tempo_animacao(self):
        return self.__tempo_animacao

    @tempo_animacao.setter
    def tempo_animacao(self, value):
        self.__tempo_animacao = value

    @property
    def contador(self):
        return self.__contador

    @contador.setter
    def contador(self, value):
        self.__contador = value

    @property
    def vento(self):
        return self.__vento

    @vento.setter
    def vento(self, value):
        self.__vento = value

    @property
    def vento_rect(self):
        return self.__vento_rect

    @vento_rect.setter
    def vento_rect(self, value):
        self.__vento_rect = value

    @property
    def subindo(self):
        return self.__subindo

    @subindo.setter
    def subindo(self, value):
        self.__subindo = value

    @property
    def tiro_triplo(self):
        return self.__tiro_triplo

    @tiro_triplo.setter
    def tiro_triplo(self, value):
        self.__tiro_triplo = value

    # endregion

    def animacao_vento(self):
        if self.subindo:
            self.vento_rect.centerx = self.rect.centerx - 1
            self.vento_rect.centery = self.rect.centery
            self.tela.display.blit(self.vento, self.vento_rect)
        
    def update(self):
        tecla = pygame.key.get_pressed()
        moveu = False
        
        # Animação da nave
        self.contador += 1
        if self.contador >= self.tempo_animacao:
            self.contador = 0
            self.indice = (self.indice + 1) % len(self.frames)
            self.image = self.frames[self.indice]
        
        if tecla[pygame.K_RIGHT] or tecla[pygame.K_d]:
            if self.rect.right < self.tela.largura:
                self.rect.right += 5
                self.subindo = False
                moveu = True

        if tecla[pygame.K_LEFT] or tecla[pygame.K_a]:
            if self.rect.left > 0:
                self.rect.left -= 5
                self.subindo = False
                moveu = True
        
        if tecla[pygame.K_UP] or tecla[pygame.K_w]:
            if self.rect.top > 0:
                self.rect.top -= 2
                self.subindo = True
                moveu = True

        if tecla[pygame.K_DOWN] or tecla[pygame.K_s]:
            if self.rect.bottom < self.tela.altura:
                self.rect.bottom += 5
                self.subindo = False
                moveu = True
        
        # Queda lenta se não se moveu para baixo
        if not moveu:
            if self.rect.bottom < self.tela.altura:
                self.rect.bottom += 1
                self.subindo = False
