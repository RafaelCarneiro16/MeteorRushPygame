import pygame
from texto import Texto

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, tipo, grupo, posicao, tela, jogador): 
        super().__init__(grupo)
        self.__tipo = tipo
        self.__tela = tela
        self.__jogador = jogador

        power_up_imagem = pygame.image.load(r'C:\GitHub\Jogo\imagens\power_up.png').convert_alpha() 
        escudo_imagem = pygame.image.load(r'C:\GitHub\Jogo\imagens\escudo.png').convert_alpha()
        
        if tipo == 'power_up':
            self.__image = power_up_imagem
            self.__rect = self.image.get_rect(center=posicao)

        elif tipo == 'escudo':
            self.__image = escudo_imagem
            self.__rect = self.image.get_rect(center=self.jogador.rect.center)
            self.__tempo_ativado = pygame.time.get_ticks()
            self.__duracao = 8000 

        elif tipo == 'tiro_triplo':
            self.__tempo_ativado = pygame.time.get_ticks()
            self.__duracao = 8000
            self.__jogador.tiro_triplo = True
            self.__image = pygame.Surface((1, 1), pygame.SRCALPHA)
            self.__image.fill((0, 0, 0, 0))
            self.__rect = self.image.get_rect(center=(-100, -100))

    
    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, value):
        self.__tipo = value

    @property
    def tela(self):
        return self.__tela

    @tela.setter
    def tela(self, value):
        self.__tela = value

    @property
    def jogador(self):
        return self.__jogador

    @jogador.setter
    def jogador(self, value):
        self.__jogador = value

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
    def tempo_ativado(self):
        return self.__tempo_ativado

    @tempo_ativado.setter
    def tempo_ativado(self, value):
        self.__tempo_ativado = value

    @property
    def duracao(self):
        return self.__duracao

    @duracao.setter
    def duracao(self, value):
        self.__duracao = value

    def update(self): 
        if self.tipo == 'power_up':
            self.rect.y += 2
            if self.rect.top > self.tela.altura: 
                self.kill()

        elif self.tipo == 'escudo':
            self.rect.center = self.jogador.rect.center 
            tempo_atual = pygame.time.get_ticks()
            if tempo_atual - self.tempo_ativado > self.duracao:
                self.kill()

        elif self.tipo == 'tiro_triplo':
            tempo_atual = pygame.time.get_ticks()
            if tempo_atual - self.tempo_ativado > self.duracao:
                self.jogador.tiro_triplo = False
                self.kill()

    def desenhar_temporizador(self):
        tempo_atual = pygame.time.get_ticks()

        if self.tipo == 'escudo':
            tempo_restante = max(0, self.duracao - (tempo_atual - self.tempo_ativado)) // 1000
            texto = Texto(24, f'Escudo: {tempo_restante}', (255, 255, 255), (740, 580), self.tela)
            texto.desenha_texto()

        elif self.tipo == 'tiro_triplo':
            tempo_restante = max(0, self.duracao - (tempo_atual - self.tempo_ativado)) // 1000
            texto = Texto(24, f'Tiro Triplo: {tempo_restante}', (255, 255, 255), (720, 580), self.tela)
            texto.desenha_texto()