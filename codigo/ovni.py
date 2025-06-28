import pygame
from tiro import Tiro

class Ovni(pygame.sprite.Sprite):
    def __init__(self, grupo, imagem, posicao, grupo_tiros : pygame.sprite.Group, jogador):
        super().__init__(grupo)
        try:
            self.__image = pygame.image.load(imagem).convert_alpha()
        except pygame.error as erro:
            print(f"⚠️ [OVNI] Falha ao carregar imagem do OVNI: {erro}")
            self.__image = pygame.Surface((50, 30), pygame.SRCALPHA)
        self.__rect = self.image.get_rect(center=posicao)
        self.__velocidade_x = 3
        self.__direcao = 1
        self.__grupo_tiros = grupo_tiros
        self.__jogador = jogador
        self.__tempo_ultimo_tiro = pygame.time.get_ticks()
        self.__delay_tiro = 1500
        self.__vida = 3
        self.__imagem_original = self.image.copy()
        self.__tempo_dano = 0
        self.__dano_duracao = 200

    #region Getters e Setters
    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, nova_imagem):
        try:
            self.__image = pygame.image.load(nova_imagem).convert_alpha()
        except pygame.error as erro:
            print(f"⚠️ [OVNI] Falha ao carregar nova imagem do OVNI: {erro}")

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
    
    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, nova_vida):
        self.__vida = nova_vida
        

    @property
    def tempo_dano(self):
        return self.__tempo_dano

    @tempo_dano.setter
    def tempo_dano(self, novo_tempo):
        self.__tempo_dano = novo_tempo

    @property
    def dano_duracao(self):
        return self.__dano_duracao

    @dano_duracao.setter
    def dano_duracao(self, nova_duracao):
        self.__dano_duracao = nova_duracao

    @property
    def imagem_original(self):
        return self.__imagem_original

    @imagem_original.setter
    def imagem_original(self, nova_imagem):
        self.__imagem_original = nova_imagem

    #endregion

    def update(self):
        self.seguir_jogador()
        # Disparo com intervalo
        agora = pygame.time.get_ticks()
        if agora - self.tempo_ultimo_tiro >= self.delay_tiro:
            self.atirar()
            self.tempo_ultimo_tiro = agora
        
        if pygame.time.get_ticks() - self.tempo_dano >= self.dano_duracao:
            self.__image = self.__imagem_original

    def atirar(self):
        posicao_tiro = self.rect.midbottom
        try:
            tiro = Tiro(posicao_tiro, self.grupo_tiros, direcao = -1, caminho_imagem = rf"C:\GitHub\Jogo\imagens\tiro_inimigo.png")
        except Exception as erro:
            print(f"⚠️ [OVNI] Erro ao criar tiro: {erro}")

    def seguir_jogador(self):
        diferenca = self.jogador.rect.centerx - self.rect.centerx
        if abs(diferenca) > 1:
           self.rect.x += self.velocidade_x if diferenca > 0 else -self.velocidade_x

    def levar_dano(self):
        self.vida -= 1
        self.tempo_dano = pygame.time.get_ticks()
        
        # Cria uma imagem vermelha temporária
        imagem_vermelha = self.imagem_original.copy()
        imagem_vermelha.fill((255, 0, 0, 100), special_flags=pygame.BLEND_RGBA_MULT)
        self.__image = imagem_vermelha