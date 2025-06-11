import pygame

class Vidas(pygame.sprite.Sprite):
    def __init__(self, qtd_vidas: int, grupo):
        super().__init__(grupo)
        self.__qtd_vidas = qtd_vidas
        self.__imagem = pygame.image.load(r'C:\GitHub\Jogo\imagens\coracao.png').convert_alpha()
        self.__image = pygame.transform.scale(self.__imagem, (50, 50))
        self.__rect = self.__image.get_rect(topright = (800, 0))

    @property 
    def qtd_vidas(self): 
        return self.__qtd_vidas
    
    @qtd_vidas.setter
    def qtd_vidas(self, valor):
        self.__qtd_vidas = valor

    @property
    def image(self):
        return self.__image
    
    @image.setter
    def image(self, novo):
        self.__image = novo

    @property
    def rect(self):
        return self.__rect
    
    @rect.setter
    def rect(self, novo):
        self.__rect = novo
    

    def exibir_vidas(self, tela, largura_tela):
        
        espaco = 10  
        for i in range(self.__qtd_vidas):
            x = largura_tela - ((i + 1) * (self.image.get_width() + espaco))
            y = 10 
            tela.blit(self.image, (x, y))
