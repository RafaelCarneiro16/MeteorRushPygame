import pygame
from tela import Tela

class Explosao(pygame.sprite.Sprite):
    def __init__(self, group, tela: Tela, posicao):
        super().__init__(group)
        try:
            self.__tela = tela
            try:
                self.__sprites = pygame.image.load(r'C:\GitHub\Jogo\imagens\explosao.png').convert_alpha()
            except pygame.error as erro_img:
                print(f"⚠️ [EXPLOSAO] Erro ao carregar imagem: {erro_img}")
                self.__sprites = None

            self.__frames = []
            if self.__sprites:
                for i in range(4):
                    frame = pygame.Surface((60, 60), pygame.SRCALPHA)
                    frame.blit(self.__sprites, (0, 0), (i * 60, 0, 60, 60))
                    self.__frames.append(frame)
            else:
                print("⚠️ [EXPLOSAO] Sprites não carregados, frames vazios.")
            
            self.__indice = 0
            if self.__frames:
                self.__image = self.frames[self.indice]
                self.__rect = self.image.get_rect(center=posicao)
            else:
                self.__image = None
                self.__rect = pygame.Rect(posicao[0], posicao[1], 60, 60)

            self.__tempo_animacao = 3
            self.__contador = 0
        except Exception as erro:
            print(f"⚠️ [EXPLOSAO] Erro no construtor: {erro}")

    # region Getters e Setters
    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, valor):
        self.__rect = valor

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, valor):
        self.__image = valor

    @property
    def tela(self):
        return self.__tela

    @tela.setter
    def tela(self, valor):
        self.__tela = valor

    @property
    def sprites(self):
        return self.__sprites

    @sprites.setter
    def sprites(self, valor):
        self.__sprites = valor

    @property
    def frames(self):
        return self.__frames

    @frames.setter
    def frames(self, valor):
        self.__frames = valor

    @property
    def indice(self):
        return self.__indice

    @indice.setter
    def indice(self, valor):
        self.__indice = valor

    @property
    def tempo_animacao(self):
        return self.__tempo_animacao

    @tempo_animacao.setter
    def tempo_animacao(self, valor):
        self.__tempo_animacao = valor

    @property
    def contador(self):
        return self.__contador

    @contador.setter
    def contador(self, valor):
        self.__contador = valor
    # endregion

    def update(self):
        try:
            self.contador += 1
            if self.contador >= self.tempo_animacao:
                self.contador = 0
                self.indice += 1

                if self.indice >= len(self.frames):
                    self.kill()
                else:
                    self.image = self.frames[self.indice]
        except Exception as erro:
            print(f"⚠️ [EXPLOSAO] Erro no update: {erro}")
