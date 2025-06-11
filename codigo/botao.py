import pygame

class Botao(pygame.sprite.Sprite):
    def __init__(self, grupo, caminho_imagem, posicao : tuple):
        super().__init__(grupo)
        self.__image = pygame.image.load(rf'caminho_imagem').convert_alpha
        self.__rect = self.__image.get_rect(center = (posicao))

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

    def conferirclique(self, mouse):
        if mouse.button == 1:
            if self.rect.collidepoint(mouse.pos):
                return True
                
        return False

