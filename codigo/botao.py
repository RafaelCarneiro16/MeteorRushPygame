import pygame

class Botao():
    def __init__(self, imagem, posicao):
        self.__imagem = imagem
        self.__posicao = posicao

    @property
    def imagem(self):
        return self.__imagem
    
    @imagem.setter
    def imagem(self, nova_imagem):
        self.__imagem =  nova_imagem

    @property
    def posicao(self):
        return self.__posicao
    
    @posicao.setter
    def posicao(self, nova_posicao):
        self.__posicao =  nova_posicao

        

