import pygame
from tiro import Tiro

class Ovni(pygame.sprite.Sprite):
    def __init__(self, grupo, imagem, posicao, grupo_tiros : pygame.sprite.Group, jogador):
        super().__init__(grupo)
        self.__image = pygame.image.load(imagem).convert_alpha()
        self.__rect = self.__image.get_rect(center=posicao)
        self.__velocidade_x = 3
        self.__direcao = 1
        self.__grupo_tiros = grupo_tiros
        self.__jogador = jogador
        self.__tempo_ultimo_tiro = pygame.time.get_ticks()
        self.__delay_tiro = 1500

    #region Getters e Setters

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, nova_imagem):
        self.__image = pygame.image.load(nova_imagem).convert_alpha()

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, nova_posicao):
        self.__rect.topleft = nova_posicao

    @property
    def velocidade_x(self):
        return self.__velocidade_x

    @velocidade_x.setter
    def velocidade_x(self, nova_velocidade):
        self.__velocidade_x = nova_velocidade

    @property
    def direcao(self):
        return self.__direcao

    @direcao.setter
    def direcao(self, nova_direcao):
        self.__direcao = nova_direcao

    @property
    def grupo_tiros(self):
        return self.__grupo_tiros

    @grupo_tiros.setter
    def grupo_tiros(self, novo_grupo):
        self.__grupo_tiros = novo_grupo

    @property
    def jogador(self):
        return self.__jogador

    @jogador.setter
    def jogador(self, novo_jogador):
        self.__jogador = novo_jogador

    @property
    def tempo_ultimo_tiro(self):
        return self.__tempo_ultimo_tiro

    @tempo_ultimo_tiro.setter
    def tempo_ultimo_tiro(self, novo_tempo):
        self.__tempo_ultimo_tiro = novo_tempo

    @property
    def delay_tiro(self):
        return self.__delay_tiro

    @delay_tiro.setter
    def delay_tiro(self, novo_delay):
        self.__delay_tiro = novo_delay

    #endregion


    def update(self):
        # Movimento horizontal
        self.rect.x += self.velocidade_x * self.direcao

        if self.rect.right >= 800 or self.rect.left <= 0:
            self.direcao *= -1

        # Disparo com intervalo
        agora = pygame.time.get_ticks()
        if agora - self.tempo_ultimo_tiro >= self.delay_tiro:
            self.atirar()
            self.tempo_ultimo_tiro = agora

    def atirar(self):
        posicao_tiro = self.rect.midbottom
        tiro = Tiro((posicao_tiro), self.grupo_tiros, direcao = -1, caminho_imagem = rf"C:\GitHub\Jogo\imagens\tiro_inimigo.png")