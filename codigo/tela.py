import pygame

class Tela():
    def __init__(self, largura, altura):
        self.__largura = largura
        self.__altura = altura
        self.__display = pygame.display.set_mode((self.__largura, self.__altura))
        self.nome_jogo = pygame.display.set_caption('Meteor Rush')
        

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