import pygame
import random
from jogador import Jogador
from tela import Tela
from tiro import Tiro
from meteoro import Meteoro
from vidas import Vidas
from som import Som

class Jogo():
    def __init__(self, tela: Tela, jogador: Jogador, grupo_jogador: pygame.sprite.GroupSingle,
                 vidas: pygame.sprite.Group, meteoro: pygame.sprite.Group, tiro: pygame.sprite.Group, som: Som):
        
        self.__tela = tela
        self.__jogador = jogador
        self.__grupo_jogador = grupo_jogador
        self.__grupo_vidas = vidas
        self.__grupo_meteoros = meteoro
        self.__grupo_tiros = tiro
        self.__clock = pygame.time.Clock()
        self.__som = som

    def novo_jogo(self):
        
        self.__grupo_vidas.empty()
        self.__grupo_meteoros.empty()
        self.__grupo_tiros.empty()

        lista_vidas = []

        # Cria vidas
        for i in range(3):
            x = self.__tela.largura - (i * (40+5))
            vida = Vidas(self.__grupo_vidas, x)
            lista_vidas.append(vida)

        pontuacao = 0
        font = pygame.font.SysFont(None, 36)

        evento_meteoro = pygame.USEREVENT + 1
        pygame.time.set_timer(evento_meteoro, 250)

        rodando = True

        #Som
        self.__som.tocar_musica(r"C:\GitHub\Jogo\sons\musica_jogo.wav")

        while rodando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        return
                    elif evento.key == pygame.K_SPACE:
                        Tiro(self.__jogador.rect.midtop, self.__grupo_tiros)
                        self.__som.tocar_efeitos(r"C:\GitHub\Jogo\sons\laser.wav")
                        

                elif evento.type == evento_meteoro:
                    x = random.randint(0, self.__tela.largura - 50)
                    Meteoro(x, self.__grupo_meteoros)

            # Colisões
            colisao_jogador = pygame.sprite.spritecollide(self.__jogador, self.__grupo_meteoros, True)
            if colisao_jogador:
                self.__som.tocar_efeitos(r"C:\GitHub\Jogo\sons\hit.wav")
                if lista_vidas:
                    vida_perdida = lista_vidas.pop()
                    vida_perdida.kill()
                    if not lista_vidas: 
                        self.__som.parar_musica()
                        self.__som.tocar_efeitos(r"C:\GitHub\Jogo\sons\game_over_efeito.wav")
                        rodando = False

            colisao = pygame.sprite.groupcollide(self.__grupo_tiros, self.__grupo_meteoros, True, True)
            for tiros, meteoros_acertados in colisao.items():
                for meteoro in meteoros_acertados:
                    pontuacao += meteoro.pontos
                    self.__som.tocar_efeitos(r"C:\GitHub\Jogo\sons\explosion.wav")

           
            # Atualizações
            self.__grupo_jogador.update(self.__tela)
            self.__grupo_tiros.update()
            self.__grupo_meteoros.update()
            self.__grupo_vidas.update()

            # Desenhos
            self.__tela.display.blit(self.__tela.imagem_fundo, self.__tela.rect_fundo)
            self.__grupo_jogador.draw(self.__tela.display)
            self.__grupo_tiros.draw(self.__tela.display)
            self.__grupo_meteoros.draw(self.__tela.display)
            self.__grupo_vidas.draw(self.__tela.display)

            texto_pontuacao = font.render(f"Pontuação: {pontuacao}", True, (255, 255, 255))
            self.__tela.display.blit(texto_pontuacao, (10, 10))

            pygame.display.update()
            self.__clock.tick(60)