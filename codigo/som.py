import pygame

        # explosao = self.__som.tocar_efeitos(r"C:\GitHub\Jogo\sons\explosion.wav")
        # laser = self.__som.tocar_efeitos(r"C:\GitHub\Jogo\sons\laser.wav")
        # power_up = self.__som.tocar_efeitos(r"C:\GitHub\Jogo\sons\power_up.wav")
        # clique_inicio = self.__som.tocar_efeitos("C:\GitHub\Jogo\sons\clique_inicio.wav")
        # musica_jogo = self.__som.tocar_musica(r"C:\GitHub\Jogo\sons\musica_jogo.wav")
        # musica_menu = self.__som.tocar_musica(r"C:\GitHub\Jogo\sons\musica_menu.wav")

class Som():
    def __init__(self):

        pygame.mixer.init()
        
    def tocar_efeitos(self, caminho, volume = 1.0):
        efeito = pygame.mixer.Sound(caminho)

        try:
            if 0.0 <= volume <= 1.0:
                efeito.set_volume(volume)
            else:
                raise ValueError("Volume fora do intervalo válido.")
        except:
            print('Volume deve estar no intervalo entre 0.0 e 1.0')

        efeito.play()
   
    def tocar_musica(self, caminho):
        pygame.mixer.music.load(caminho)
        pygame.mixer.music.play(-1)

    def parar_musica(self):
        pygame.mixer.music.stop()




