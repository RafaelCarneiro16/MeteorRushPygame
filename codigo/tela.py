import pygame

class Tela():
    def __init__(self, largura, altura, imagem_fundo):
        self.__largura = largura
        self.__altura = altura
        self.__display = pygame.display.set_mode((self.__largura, self.__altura))
        self.nome_jogo = pygame.display.set_caption('Meteor Rush')
        self.__imagem_fundo = pygame.image.load(rf'{imagem_fundo}').convert_alpha()
        self.__rect_fundo = self.__imagem_fundo.get_rect(center = (400,300))

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

    #endregion                     