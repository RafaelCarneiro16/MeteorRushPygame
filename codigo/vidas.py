import pygame

class Vidas():
    def __init__(self, qtd_vidas:int):
        self.__qtd_vidas = qtd_vidas
        self.__imagem = pygame.image.load(rf'C:\GitHub\Jogo\imagens\coracao.png')
        self.__imagem_redimensionada = pygame.transform.scale(self.__imagem, (50, 50))

    @property 
    def qtd_vidas(self): 
        return self.__qtd_vidas
    
    @qtd_vidas.setter
    def qtd_vidas(self, valor):
        self.__qtd_vidas = valor

    @property 
    def imagem(self): 
        return self.__imagem
    
    @imagem.setter
    def imagem(self, valor):
        self.__imagem = valor

    @property 
    def imagem_redimensionada(self): 
        return self.__imagem_redimensionada
    
    @imagem_redimensionada.setter
    def imagem_redimensionada(self, valor):
        self.__imagem_redimensionada = valor

    def exibir_vidas(self):
        
        