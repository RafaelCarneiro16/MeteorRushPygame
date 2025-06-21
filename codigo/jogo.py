import pygame
import random
from jogador import Jogador
from tela import Tela
from tiro import Tiro
from meteoro import Meteoro
from vidas import Vidas
from som import Som
from meteorodourado import Meteoro_Dourado
from botao import Botao
from jogador_ranking import JogadorRanking
from gerenciador_raking import GerenciadorRanking
from cenario import Cenario

class Jogo():
    def __init__(self, tela: Tela, jogador: Jogador, grupo_jogador: pygame.sprite.GroupSingle,
                 vidas: pygame.sprite.Group, meteoro: pygame.sprite.Group, tiro: pygame.sprite.Group, som: Som,
                 meteoros_dourados : pygame.sprite.Group):

        self.__tela = tela
        self.__jogador = jogador
        self.__grupo_jogador = grupo_jogador
        self.__grupo_vidas = vidas
        self.__grupo_meteoros = meteoro
        self.__grupo_tiros = tiro
        self.__clock = pygame.time.Clock()
        self.__som = som
        self.__grupo_meteoros_dourados = meteoros_dourados
        self.__ranking = GerenciadorRanking()
        self.__ranking.carregar_de_arquivo("ranking.json")
        self.__cenario = Cenario(self.__tela)

    #region Setters e Getters
    @property
    def cenario(self):
        return self.__cenario

    @cenario.setter
    def cenario(self, value):
        self.__cenario = value

    @property
    def tela(self):
        return self.__tela

    @tela.setter
    def tela(self, value):
        self.__tela = value

    @property
    def jogador(self):
        return self.__jogador

    @jogador.setter
    def jogador(self, value):
        self.__jogador = value

    @property
    def grupo_jogador(self):
        return self.__grupo_jogador

    @grupo_jogador.setter
    def grupo_jogador(self, value):
        self.__grupo_jogador = value

    @property
    def grupo_vidas(self):
        return self.__grupo_vidas

    @grupo_vidas.setter
    def grupo_vidas(self, value):
        self.__grupo_vidas = value

    @property
    def grupo_meteoros(self):
        return self.__grupo_meteoros

    @grupo_meteoros.setter
    def grupo_meteoros(self, value):
        self.__grupo_meteoros = value

    @property
    def grupo_tiros(self):
        return self.__grupo_tiros

    @grupo_tiros.setter
    def grupo_tiros(self, value):
        self.__grupo_tiros = value

    @property
    def clock(self):
        return self.__clock

    @clock.setter
    def clock(self, value):
        self.__clock = value

    @property
    def som(self):
        return self.__som

    @som.setter
    def som(self, value):
        self.__som = value

    @property
    def grupo_meteoros_dourados(self):
        return self.__grupo_meteoros_dourados

    @grupo_meteoros_dourados.setter
    def grupo_meteoros_dourados(self, value):
        self.__grupo_meteoros_dourados = value
    #endregion

    def novo_jogo(self):
        self.grupo_vidas.empty()
        self.grupo_meteoros.empty()
        self.grupo_tiros.empty()
        self.grupo_meteoros_dourados.empty()

        grupo_pause = pygame.sprite.GroupSingle()
        botao_pause = Botao(grupo_pause, r'C:\GitHub\Jogo\imagens\pause.png', (60, 560))

        lista_vidas = []

        # Cria vidas
        for i in range(3):
            x = self.tela.largura - (i * (40+5))
            vida = Vidas(self.grupo_vidas, x)
            lista_vidas.append(vida)

        pontuacao = 0
        font = pygame.font.Font(r'C:\GitHub\Jogo\fonte.ttf', 24)

        evento_meteoro = pygame.USEREVENT + 1
        evento_meteoro_dourado = pygame.USEREVENT + 2
        pygame.time.set_timer(evento_meteoro, 250)
        pygame.time.set_timer(evento_meteoro_dourado, 2000)

        # Posições do fundo animado
        y1 = 0
        y2 = -self.__tela.altura
        velocidade_fundo = 2

        rodando = True

        # Som
        self.__som.tocar_musica(rf"C:\GitHub\Jogo\sons\musica_jogo.wav")

        while rodando:

            mouse_pos = pygame.mouse.get_pos()
            mouse_botao = pygame.mouse.get_pressed()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        return
                    elif evento.key == pygame.K_SPACE:
                        Tiro(self.jogador.rect.midtop, self.grupo_tiros)
                        self.som.tocar_efeitos(rf"C:\GitHub\Jogo\sons\laser.wav")

                elif evento.type == evento_meteoro:
                    x = random.randint(0, self.tela.largura - 50)
                    Meteoro(x, self.grupo_meteoros)

                elif evento.type == evento_meteoro_dourado:
                    x = random.randint(0, self.tela.largura - 50)
                    Meteoro_Dourado(x, self.grupo_meteoros_dourados)

            if mouse_botao[0]:
                if botao_pause.rect.collidepoint(mouse_pos):
                    resultado = self.pause()
                    if not resultado:
                        return      

            # Atualizar posição do fundo
            y1 += velocidade_fundo
            y2 += velocidade_fundo

            if y1 >= self.tela.altura:
                y1 = -self.tela.altura
            if y2 >= self.tela.altura:
                y2 = -self.tela.altura

            # Colisões
            colisao_jogador_m = pygame.sprite.spritecollide(self.jogador, self.grupo_meteoros, True)
            colisao_jogador_md = pygame.sprite.spritecollide(self.jogador, self.grupo_meteoros_dourados, True)

            if colisao_jogador_m or colisao_jogador_md:
                self.som.tocar_efeitos(r"C:\GitHub\Jogo\sons\hit.wav")
                if lista_vidas:
                    vida_perdida = lista_vidas.pop()
                    vida_perdida.kill()
                    if not lista_vidas: 
                        self.som.parar_musica()
                        self.som.tocar_efeitos(r"C:\GitHub\Jogo\sons\game_over_efeito.wav")

                        nome = self.__ranking.solicitar_nome(self.__tela, self.__clock)  # Pede o nome
                        self.__ranking.adicionar_jogador(JogadorRanking(nome, pontuacao))  # Adiciona o jogador com pontuação
                        self.__ranking.salvar_em_arquivo("ranking.json")  # Salva o ranking

                        self.game_over()
                        rodando = False

            pontuacao = self.colisao_meteoro(self.grupo_tiros, self.grupo_meteoros, pontuacao)
            pontuacao = self.colisao_meteoro(self.grupo_tiros, self.grupo_meteoros_dourados, pontuacao)

            # Atualizações dos grupos
            self.grupo_jogador.update()
            self.grupo_tiros.update()
            self.grupo_meteoros.update()
            self.grupo_vidas.update()
            self.grupo_meteoros_dourados.update()
            grupo_pause.update()

            # Desenhar fundo com rolagem
            self.tela.display.blit(self.tela.imagem_fundo, (0, y1))
            self.tela.display.blit(self.tela.imagem_fundo, (0, y2))

            # Atualizar e desenhar o cenário 
            self.__cenario.update()
            self.__cenario.draw(self.tela.display)

            # Desenhos
            self.grupo_jogador.draw(self.tela.display)
            self.jogador.animacao_vento()
            self.grupo_tiros.draw(self.tela.display)
            self.grupo_meteoros.draw(self.tela.display)
            self.grupo_vidas.draw(self.tela.display)
            self.grupo_meteoros_dourados.draw(self.tela.display)
            grupo_pause.draw(self.tela.display)

            texto_pontuacao = font.render(f"Pontuação: {pontuacao}", True, (255, 255, 255))
            self.tela.display.blit(texto_pontuacao, (10, 10))

            pygame.display.update()
            self.clock.tick(60)


    def pause(self):
        grupo_botoes = pygame.sprite.Group()
        pausado = True
        titulo = Botao(grupo_botoes, rf'C:\GitHub\Jogo\imagens\titulo_jogo_pausado.png', (400, 100))
        botao_voltar = Botao(grupo_botoes, rf'C:\GitHub\Jogo\imagens\bt_voltar_ao_jogo.png', (400, 200))
        botao_menu = Botao(grupo_botoes, rf'C:\GitHub\Jogo\imagens\bt_menu_principal.png', (400, 320))
        botao_sair = Botao(grupo_botoes, rf'C:\GitHub\Jogo\imagens\bt_salvar_sair.png', (400, 440))

        fundo_transparente = pygame.Surface((800,600))
        fundo_transparente.set_alpha(120)
        fundo_transparente.fill((0, 0, 0))
        fundo_congelado = self.tela.display.copy()

        while pausado:
            mouse_pos = pygame.mouse.get_pos()
            mouse_botao = pygame.mouse.get_pressed()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            if mouse_botao[0]:
                if botao_menu.rect.collidepoint(mouse_pos):
                    self.som.tocar_efeitos(r"C:\GitHub\Jogo\sons\clique.mp3")
                    return False
                elif botao_voltar.rect.collidepoint(mouse_pos):
                    self.som.tocar_efeitos(r"C:\GitHub\Jogo\sons\clique.mp3")
                    return True
                elif botao_sair.rect.collidepoint(mouse_pos):
                    self.som.tocar_efeitos(r"C:\GitHub\Jogo\sons\clique.mp3")
                    pygame.quit()
                    exit()

            self.tela.display.blit(fundo_congelado,(0,0))
            self.tela.display.blit(fundo_transparente, (0,0))
            grupo_botoes.update()
            grupo_botoes.draw(self.tela.display)

            pygame.display.update()
            self.clock.tick(15)

    def colisao_meteoro(self, grupo_tiros , grupo_meteoros, pontuacao):
        colisao = pygame.sprite.groupcollide(grupo_tiros, grupo_meteoros, True, True)
        for tiros, meteoros_acertados in colisao.items():
            for meteoro in meteoros_acertados:
                pontuacao += meteoro.pontos
                self.som.tocar_efeitos(r"C:\GitHub\Jogo\sons\explosion.wav")
        return pontuacao        

    def game_over(self):
        grupo_botoes = pygame.sprite.Group()
        pausado = True
        botao_novo_jogo = Botao(grupo_botoes, rf'C:\GitHub\Jogo\imagens\bt_novo_jogo.png', (400, 200))
        botao_menu = Botao(grupo_botoes, rf'C:\GitHub\Jogo\imagens\bt_menu_principal.png', (400, 320))
        botao_sair = Botao(grupo_botoes, rf'C:\GitHub\Jogo\imagens\bt_salvar_sair.png', (400, 440))

        fundo_transparente = pygame.Surface((800,600))
        fundo_transparente.set_alpha(120)
        fundo_transparente.fill((0, 0, 0))
        fundo_congelado = self.tela.display.copy()

        while pausado:
            mouse_pos = pygame.mouse.get_pos()
            mouse_botao = pygame.mouse.get_pressed()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            if mouse_botao[0]:
                if botao_menu.rect.collidepoint(mouse_pos):
                    self.som.tocar_efeitos(r"C:\GitHub\Jogo\sons\clique.mp3")
                    return
                elif botao_novo_jogo.rect.collidepoint(mouse_pos):
                    self.som.tocar_efeitos(r"C:\GitHub\Jogo\sons\clique.mp3")
                    self.novo_jogo()
                    return
                elif botao_sair.rect.collidepoint(mouse_pos):
                    self.som.tocar_efeitos(r"C:\GitHub\Jogo\sons\clique.mp3")
                    pygame.quit()
                    exit()

            self.tela.display.blit(fundo_congelado,(0,0))
            self.tela.display.blit(fundo_transparente, (0,0))
            grupo_botoes.update()
            grupo_botoes.draw(self.tela.display)

            pygame.display.update()
            self.clock.tick(15)

    def cria_explosao(self, posicao):
        explosao = pygame.image.load(r'C:\GitHub\Jogo\imagens\5.png')
        self.tela.display.blit(explosao, (posicao))
