import pygame
from tela import Tela

class Cenario(pygame.sprite.Group):
    def __init__(self, tela: Tela):
        super().__init__()
        try:
            self.__tela = tela

            try:
                self.__imagem_planeta = pygame.image.load(r"C:\GitHub\Jogo\imagens\planeta.png").convert_alpha()
            except pygame.error as erro_img_planeta:
                print(f"⚠️ [CENARIO] Erro ao carregar imagem do planeta: {erro_img_planeta}")
                self.__imagem_planeta = None

            try:
                self.__imagem_sol = pygame.image.load(r"C:\GitHub\Jogo\imagens\sol.png").convert_alpha()
            except pygame.error as erro_img_sol:
                print(f"⚠️ [CENARIO] Erro ao carregar imagem do sol: {erro_img_sol}")
                self.__imagem_sol = None

            self.__sprite = pygame.sprite.Sprite()
            if self.__imagem_planeta:
                self.__sprite.image = self.__imagem_planeta
                self.__sprite.rect = self.__sprite.image.get_rect(topleft=(-999, -999))  # Fora da tela (Não aparecer)
            else:
                self.__sprite.image = None
                self.__sprite.rect = pygame.Rect(-999, -999, 0, 0)

            self.add(self.__sprite)

            self.__mostrando = False
            self.__modo_atual = "planeta"
            self.__proximo_evento = pygame.time.get_ticks() + 5000  # Tempo entre o sol e o planeta
        except Exception as erro:
            print(f"⚠️ [CENARIO] Erro no construtor: {erro}")

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
        try:
            agora = pygame.time.get_ticks()

            if not self.mostrando:
                if agora >= self.proximo_evento:
                    if self.modo_atual == "planeta":
                        if self.imagem_planeta:
                            self.sprite.image = self.imagem_planeta
                            self.sprite.rect = self.sprite.image.get_rect(topleft=(-100, -self.sprite.image.get_height()))
                        else:
                            print("⚠️ [CENARIO] Imagem do planeta não carregada.")
                        self.modo_atual = "sol"
                    else:
                        if self.imagem_sol:
                            self.sprite.image = self.imagem_sol
                            self.sprite.rect = self.sprite.image.get_rect(topleft=(680, -self.sprite.image.get_height()))
                        else:
                            print("⚠️ [CENARIO] Imagem do sol não carregada.")
                        self.modo_atual = "planeta"

                    self.mostrando = True
            else:
                self.sprite.rect.y += 1
                if self.sprite.rect.top > self.tela.altura:
                    self.sprite.rect.topleft = (-999, -999)
                    self.mostrando = False
                    self.proximo_evento = agora + 5000
        except Exception as erro:
            print(f"⚠️ [CENARIO] Erro no update: {erro}")
