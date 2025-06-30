import pygame 
from texto import Texto
import os

class Som():
    def __init__(self):
        pygame.mixer.init()  

        self.__volume_efeitos = 0.5        
        self.__volume_musica = 0.5         
        self.__volume_geral = 1.0     
         
        self.__largura_barra_volume = 200
        self.__altura_barra_volume = 10
        self.__x_barra_volume = 300
        self.__y_barra_musica = 200
        self.__y_barra_efeitos = 300
        self.__arrastando_musica = False
        self.__arrastando_efeitos = False

        self.__cursor_musica = pygame.Rect(
            self.x_barra_volume + int(self.volume_musica * self.largura_barra_volume) - 5,
            self.y_barra_musica - 5,
            10, 20
        )
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
        try:
            pygame.mixer.music.set_volume(self.__volume_musica)
        except pygame.error as erro:
            print(f"⚠️ [SOM] Erro pygame: {erro}")

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
    # endregion

    # Atualiza o volume da música considerando o volume geral
    def atualizar_volumes(self):
        try:
            pygame.mixer.music.set_volume(self.volume_musica * self.volume_geral)
        except pygame.error as erro:
            print(f"⚠️ [SOM] Erro pygame: {erro}")
    
    # Toca um efeito sonoro com volume opcional
    def tocar_efeitos(self, som, volume=None):
        try:
            efeito = pygame.mixer.Sound(os.path.join('sons', f'{som}'))
            if volume is None:
                volume = self.__volume_efeitos
            efeito.set_volume(volume)
            efeito.play()
        except pygame.error as erro:
            print(f"⚠️ [SOM] Erro pygame: {erro}")
        except FileNotFoundError:
            print(f"⚠️ [SOM] Arquivo não encontrado: {som}")

    # Carrega e toca uma música em loop com volume opcional
    def tocar_musica(self, som, volume=None):
        try:
            pygame.mixer.music.load(os.path.join('sons', f'{som}'))
            if volume is None:
                volume = self.__volume_musica
            pygame.mixer.music.set_volume(volume)
            pygame.mixer.music.play(-1)
        except pygame.error as erro:
            print(f"⚠️ [SOM] Erro pygame: {erro}")
        except FileNotFoundError:
            print(f"⚠️ [SOM] Arquivo não encontrado: {som}")

    # Para a música que estiver tocando
    def parar_musica(self):
        try:
            pygame.mixer.music.stop()
        except pygame.error as erro:
            print(f"⚠️ [SOM] Erro pygame: {erro}")

    # Atualiza a posição dos sliders conforme o movimento do mouse
    def atualizar_sliders(self, mouse_x):
        if self.arrastando_musica:
            self.cursor_musica.centerx = max(
                self.x_barra_volume,
                min(mouse_x, self.x_barra_volume + self.largura_barra_volume)
            )
            novo_volume = (self.cursor_musica.centerx - self.x_barra_volume) / self.largura_barra_volume
            self.volume_musica = novo_volume

        if self.arrastando_efeitos:
            self.cursor_efeitos.centerx = max(
                self.x_barra_volume,
                min(mouse_x, self.x_barra_volume + self.largura_barra_volume)
            )
            novo_volume = (self.cursor_efeitos.centerx - self.x_barra_volume) / self.largura_barra_volume
            self.volume_efeitos = novo_volume
            self.atualizar_volumes()

    # Exibe o menu de volume com sliders interativos para música e efeitos
    def exibir_menu_volume(self, tela, clock, texto_titulo, texto_instrucao):
        rodando = True

        while rodando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                    rodando = False
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    if self.cursor_musica.collidepoint(pygame.mouse.get_pos()):
                        self.arrastando_musica = True
                    if self.cursor_efeitos.collidepoint(pygame.mouse.get_pos()):
                        self.arrastando_efeitos = True
                elif evento.type == pygame.MOUSEBUTTONUP:
                    self.arrastando_musica = False
                    self.arrastando_efeitos = False

            mouse_x = pygame.mouse.get_pos()[0]
            self.atualizar_sliders(mouse_x)

            texto_musica = Texto(
                24,
                f'Música: {int(self.volume_musica * 100)}%',
                (255, 255, 255),
                (self.x_barra_volume + self.largura_barra_volume // 2, self.y_barra_musica - 20),
                tela)

            texto_efeitos = Texto(
                24,
                f'Efeitos: {int(self.volume_efeitos * 100)}%',
                (255, 255, 255),
                (self.x_barra_volume + self.largura_barra_volume // 2, self.y_barra_efeitos - 20),
                tela)

            tela.display.blit(tela.imagem_fundo, tela.rect_fundo)
            texto_instrucao.desenha_texto()
            texto_titulo.desenha_texto()

            pygame.draw.rect(tela.display, (200, 200, 200), (self.x_barra_volume, self.y_barra_musica, self.largura_barra_volume, self.altura_barra_volume))
            pygame.draw.rect(tela.display, (255, 255, 255), self.cursor_musica)

            pygame.draw.rect(tela.display, (200, 200, 200), (self.x_barra_volume, self.y_barra_efeitos, self.largura_barra_volume, self.altura_barra_volume))
            pygame.draw.rect(tela.display, (255, 255, 255), self.cursor_efeitos)

            texto_musica.desenha_texto()
            texto_efeitos.desenha_texto()

            pygame.display.flip()
            clock.tick(60)
