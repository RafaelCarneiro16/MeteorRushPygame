import pygame
from tela import Tela
from jogador import Jogador

class Tiro(pygame.sprite.Sprite):
    def init(self, posição : tuple, grupo, direcao, caminho_imagem = None):
        super().init(grupo)

        if caminho_imagem is None:
            caminho_imagem = rf"C:\GitHub\Jogo\imagens\tiro_jogador.png"

        self.image = pygame.image.load(caminho_imagem).convert_alpha()
        self.rect = self.image.get_rect(center = (posição))
        self.direcao = direcao

    @property
    def image(self):
        return self.image

    @image.setter
    def image(self, nova_imagem):
        self.image = nova_imagem 

    @property
    def rect(self):
        return self.rect

    @rect.setter
    def rect(self, novo):
        self.rect = novo

    @property
    def direcao(self):
        return self.direcao

    @direcao.setter
    def direcao(self, novo):
        self.direcao = novo

    def draw(self, tela: Tela):
        tela.display.blit(self.image, self.rect)

    def update(self):
        self.rect.y -= self.direcao * 10
        if self.rect.bottom < 0:
           self.kill()