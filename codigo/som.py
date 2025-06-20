import pygame  

class Som():
    def __init__(self):
        pygame.mixer.init()  

        self.__volume_efeitos = 0.5        
        self.__volume_musica = 0.5         
        self.__volume_geral = 1.0     
         
        # Volume
        self.__largura_barra_volume = 200
        self.__altura_barra_volume = 10
        self.__x_barra_volume = 300
        self.__y_barra_musica = 200
        self.__y_barra_efeitos = 300
        self.__arrastando_musica = False
        self.__arrastando_efeitos = False

        # Cursor de volume música
        self.__cursor_musica = pygame.Rect(
            self.x_barra_volume + int(self.volume_musica * self.largura_barra_volume) - 5,
            self.y_barra_musica - 5,
            10, 20
        )

        # Cursor de volume efeitos
        self.__cursor_efeitos = pygame.Rect(
            self.x_barra_volume + int(self.volume_efeitos * self.largura_barra_volume) - 5,
            self.y_barra_efeitos - 5,
            10, 20
        )
    
    # region Getters e Setters
   
    @property
    def volume_geral(self):
        return self.__volume_geral
    
    @volume_geral.setter
    def volume_geral(self, valor):
        self.__volume_geral = max(0.0, min(1.0, valor)) 
        self.atualizar_volumes()

    @property
    def volume_efeitos(self):
        return self.__volume_efeitos
    
    @volume_efeitos.setter
    def volume_efeitos(self, valor):
        self.__volume_efeitos = max(0.0, min(1.0, valor))

    @property
    def volume_musica(self):
        return self.__volume_musica
    
    @volume_musica.setter
    def volume_musica(self, valor):
        self.__volume_musica = max(0.0, min(1.0, valor))
        pygame.mixer.music.set_volume(self.__volume_musica)

    @property
    def largura_barra_volume(self):
        return self.__largura_barra_volume

    @largura_barra_volume.setter
    def largura_barra_volume(self, valor):
        self.__largura_barra_volume = valor

    @property
    def altura_barra_volume(self):
        return self.__altura_barra_volume

    @altura_barra_volume.setter
    def altura_barra_volume(self, valor):
        self.__altura_barra_volume = valor

    @property
    def x_barra_volume(self):
        return self.__x_barra_volume

    @x_barra_volume.setter
    def x_barra_volume(self, valor):
        self.__x_barra_volume = valor

    @property
    def y_barra_musica(self):
        return self.__y_barra_musica

    @y_barra_musica.setter
    def y_barra_musica(self, valor):
        self.__y_barra_musica = valor

    @property
    def y_barra_efeitos(self):
        return self.__y_barra_efeitos

    @y_barra_efeitos.setter
    def y_barra_efeitos(self, valor):
        self.__y_barra_efeitos = valor

    @property
    def arrastando_musica(self):
        return self.__arrastando_musica

    @arrastando_musica.setter
    def arrastando_musica(self, valor):
        self.__arrastando_musica = valor

    @property
    def arrastando_efeitos(self):
        return self.__arrastando_efeitos

    @arrastando_efeitos.setter
    def arrastando_efeitos(self, valor):
        self.__arrastando_efeitos = valor

    @property
    def cursor_musica(self):
        return self.__cursor_musica

    @cursor_musica.setter
    def cursor_musica(self, valor):
        self.__cursor_musica = valor

    @property
    def cursor_efeitos(self):
        return self.__cursor_efeitos

    @cursor_efeitos.setter
    def cursor_efeitos(self, valor):
        self.__cursor_efeitos = valor

     # Comentario usado para minimizar Setters e Getters
    # endregion

    def atualizar_volumes(self):
        pygame.mixer.music.set_volume(self.volume_musica * self.volume_geral)
    
    def tocar_efeitos(self, caminho, volume=None):
        efeito = pygame.mixer.Sound(caminho)  
        if volume is None:
            volume = self.__volume_efeitos  
        efeito.set_volume(volume)        
        efeito.play()                      

    def tocar_musica(self, caminho, volume=None):
        pygame.mixer.music.load(caminho)     
        if volume is None:
            volume = self.__volume_musica    
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1)         

    def parar_musica(self):
        pygame.mixer.music.stop()
