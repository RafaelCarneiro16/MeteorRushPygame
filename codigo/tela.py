import pygame
import os

class Tela():
    def __init__(self, largura, altura, imagem_fundo):
        try:
            self.__largura = largura
            self.__altura = altura
            self.__display = pygame.display.set_mode((self.largura, self.altura))
            self.__nome_jogo = pygame.display.set_caption('Meteor Rush')
            try:
                self.__imagem_fundo = pygame.image.load(os.path.join('imagens', f'{imagem_fundo}')).convert_alpha()
            except pygame.error as erro_img:
                print(f"⚠️ [TELA] Erro ao carregar imagem: {erro_img}")
                self.__imagem_fundo = None
            self.__rect_fundo = self.imagem_fundo.get_rect(center=(400, 300)) if self.imagem_fundo else None
        except pygame.error as erro:
            print(f"⚠️ [TELA] Erro pygame: {erro}")

        # Variáveis internas para rolagem do fundo
        self.__y1 = 0
        self.__y2 = -self.__altura
        
    #region Setters e Getters
    @property
    def largura(self):
        return self.__largura

    @largura.setter
    def largura(self, nova):
        self.__largura = nova

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, nova):
        self.__altura = nova    

    @property
    def display(self):
        return self.__display

    @display.setter
    def display(self, novo):
        self.__display = novo

    @property
    def imagem_fundo(self):
        return self.__imagem_fundo

    @imagem_fundo.setter
    def imagem_fundo(self, nova):
        self.__imagem_fundo = nova

    @property
    def rect_fundo(self):
        return self.__rect_fundo

    @rect_fundo.setter
    def rect_fundo(self, novo):
        self.__rect_fundo = novo

    @property
    def nome_jogo(self):
        return self.__nome_jogo

    @nome_jogo.setter
    def nome_jogo(self, novo):
        self.__nome_jogo = novo

    @property
    def y1(self):
        return self.__y1

    @y1.setter
    def y1(self, novo):
        self.__y1 = novo
    
    @property
    def y2(self):
        return self.__y2

    @y2.setter
    def y2(self, novo):
        self.__y2 = novo
    #endregion

    def fundo_mover(self):
        try:
            # Atualiza posições
            self.y1 += 2
            self.y2 += 2

            # Reinicia posições quando saem da tela
            if self.y1 >= self.altura:
                self.y1 = -self.altura
            if self.y2 >= self.altura:
                self.y2 = -self.altura

            # Desenha os fundos (se imagem carregada)
            if self.imagem_fundo and self.display:
                self.display.blit(self.imagem_fundo, (0, self.y1))
                self.display.blit(self.imagem_fundo, (0, self.y2))
        except Exception as erro:
            print(f"⚠️ [TELA] Erro ao mover fundo: {erro}")
