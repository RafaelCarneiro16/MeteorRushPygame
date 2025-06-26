import pygame
from tiro import Tiro  # Supondo que já existe essa classe

class Inimigo(pygame.sprite.Sprite):
    def __init__(self, grupo, caminho_imagem, posicao, grupo_tiros, jogador):
        super().__init__(grupo)
        self.image = pygame.image.load(rf"C:\GitHub\Jogo\imagens\ovni.png").convert_alpha()
        self.rect = self.image.get_rect(center=posicao)
        self.velocidade = 2
        self.grupo_tiros = grupo_tiros
        self.jogador = jogador
        self.tempo_ultimo_tiro = pygame.time.get_ticks()
        self.delay_tiro = 1500  # milissegundos

    def update(self):
        # Movimento simples (vertical)
        self.rect.y += self.velocidade
        if self.rect.top > 600:  # Saiu da tela
            self.rect.bottom = 0

        # Atirar
        agora = pygame.time.get_ticks()
        if agora - self.tempo_ultimo_tiro >= self.delay_tiro:
            self.atirar()
            self.tempo_ultimo_tiro = agora

    def atirar(self):
        # Cria tiro na direção do jogador (vertical por simplicidade)
        posicao_tiro = self.rect.midbottom
        tiro = Tiro(posicao_tiro, 5, "inimigo")  # velocidade positiva: pra baixo
        self.grupo_tiros.add(tiro)
