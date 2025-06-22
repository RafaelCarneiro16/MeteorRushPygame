import pygame 
import random
from tela import Tela

class Meteoro_Dourado(pygame.sprite.Sprite):
    def __init__(self, grupo, tela: Tela, jogador):
        super().__init__(grupo)
        self.tela = tela
        self.jogador = jogador 
        self.image = pygame.image.load(r'C:\GitHub\Jogo\imagens\meteoro_dourado.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, tela.largura), -50)
        self.pos = pygame.Vector2(self.rect.center)
        self.pontos = 500 
        self.seguindo = True

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