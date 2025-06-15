import pygame
from tela import Tela
from jogo import Jogo
from botao import Botao
from som import Som

class Menu():
    def __init__(self, jogo: Jogo, tela: Tela, grupo_botoes: pygame.sprite.Group, som: Som):
        self.__clock = pygame.time.Clock()
        self.__tela = tela  
        self.__jogo = jogo
        self.__grupo_botoes = grupo_botoes
        self.__logo_jogo = pygame.image.load('C:/GitHub/Jogo/imagens/icone_nome_jogo.png').convert_alpha()
        self.__logo_rect = self.__logo_jogo.get_rect(center = (400, 125))
        self.__som = som

        # Fontes e textos fixos
        self.__fonte_titulo = pygame.font.SysFont(None, 48)
        self.__fonte_instrucao = pygame.font.SysFont(None, 24)
        self.__fonte = pygame.font.SysFont('Courier New', 24)

        self.__texto_titulo = self.__fonte_titulo.render("Gerenciador de Som", True, (255, 255, 255))
        self.__texto_instrucao = self.__fonte_instrucao.render("Pressione ESC para voltar ao menu principal", True, (255, 255, 255))

        # Retângulos para centralizar textos
        self.__ret_titulo = self.__texto_titulo.get_rect(center=(self.__tela.display.get_width() // 2, 50))
        self.__ret_instrucao = self.__texto_instrucao.get_rect(center=(self.__tela.display.get_width() // 2, self.__tela.display.get_height() - 30))

    # region Getters e Setters
    @property
    def clock(self):
        return self.__clock

    @clock.setter
    def clock(self, novo):
        self.__clock = novo

    @property
    def tela(self):
        return self.__tela

    @tela.setter
    def tela(self, nova):
        self.__tela = nova

    @property
    def jogo(self):
        return self.__jogo

    @jogo.setter
    def jogo(self, novo):
        self.__jogo = novo

    @property
    def som(self):
        return self.__som
    
    @som.setter
    def som(self, valor):
        self.__som = valor
    
    # Comentario usado para minimizar Setters e Getters
    # endregion

    # Desenha a imagem de fundo do menu
    def desenha_menu(self):
        self.tela.display.blit(self.tela.imagem_fundo, self.tela.rect_fundo)

    # Abre a tela de ajuste de volumes
    def menu_volume(self):
        rodando = True

        while rodando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                    rodando = False
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    # Verifica se o cursor de música ou efeitos está sendo arrastado
                    if self.__som.cursor_musica.collidepoint(pygame.mouse.get_pos()):
                        self.__som.arrastando_musica = True
                    if self.__som.cursor_efeitos.collidepoint(pygame.mouse.get_pos()):
                        self.__som.arrastando_efeitos = True
                elif evento.type == pygame.MOUSEBUTTONUP:
                    self.__som.arrastando_musica = False
                    self.__som.arrastando_efeitos = False

            # Pega a posição atual do mouse
            mouse_x = pygame.mouse.get_pos()[0]

            # Atualiza posição e volume da música
            if self.__som.arrastando_musica:
                self.__som.cursor_musica.centerx = max(self.__som.x_barra_volume, min(mouse_x, self.__som.x_barra_volume + self.__som.largura_barra_volume))
                novo_volume = (self.__som.cursor_musica.centerx - self.__som.x_barra_volume) / self.__som.largura_barra_volume
                self.__som.volume_musica = novo_volume

            # Atualiza posição e volume dos efeitos
            if self.__som.arrastando_efeitos:
                self.__som.cursor_efeitos.centerx = max(self.__som.x_barra_volume, min(mouse_x, self.__som.x_barra_volume + self.__som.largura_barra_volume))
                novo_volume = (self.__som.cursor_efeitos.centerx - self.__som.x_barra_volume) / self.__som.largura_barra_volume
                self.__som.volume_efeitos = novo_volume
                self.__som.atualizar_volumes()

            # Textos dinâmicos com os valores de volume
            texto1 = self.__fonte.render(f'Música: {int(self.__som.volume_musica * 100)}%', True, (255, 255, 255))
            texto2 = self.__fonte.render(f'Efeitos: {int(self.__som.volume_efeitos * 100)}%', True, (255, 255, 255))

            # Desenha tela de fundo e textos
            self.__tela.display.blit(self.__tela.imagem_fundo, self.__tela.rect_fundo)
            self.__tela.display.blit(self.__texto_titulo, self.__ret_titulo)
            self.__tela.display.blit(self.__texto_instrucao, self.__ret_instrucao)

            # Desenha barras e cursores de volume
            pygame.draw.rect(self.__tela.display, (200, 200, 200), (self.__som.x_barra_volume, self.__som.y_barra_musica, self.__som.largura_barra_volume, self.__som.altura_barra_volume))
            pygame.draw.rect(self.__tela.display, (255, 255, 255), self.__som.cursor_musica)

            pygame.draw.rect(self.__tela.display, (200, 200, 200), (self.__som.x_barra_volume, self.__som.y_barra_efeitos, self.__som.largura_barra_volume, self.__som.altura_barra_volume))
            pygame.draw.rect(self.__tela.display, (255, 255, 255), self.__som.cursor_efeitos)

            # Desenha os textos dos volumes
            self.__tela.display.blit(texto1, (self.__som.x_barra_volume, self.__som.y_barra_musica - 40))
            self.__tela.display.blit(texto2, (self.__som.x_barra_volume, self.__som.y_barra_efeitos - 40))

            pygame.display.flip()
            self.__clock.tick(60)

    # Tela principal do menu do jogo
    def rodando_menu(self):
        # Cria os botões do menu
        botao_novojogo = Botao(self.__grupo_botoes, 'C:/GitHub/Jogo/imagens/bt_novo_jogo.png', (400, 200))
        botao_continuar = None  # Pode ser adicionado futuramente
        botao_ranking = Botao(self.__grupo_botoes, 'C:/GitHub/Jogo/imagens/bt_ranking.png', (400, 320))
        botao_som = Botao(self.__grupo_botoes, 'C:/GitHub/Jogo/imagens/bt_som.png', (400, 442))

        # Inicia a música do menu
        self.__som.tocar_musica(r"C:\GitHub\Jogo\sons\musica_menu.wav")

        rodando_menu = True

        while rodando_menu:
            mouse_pos = pygame.mouse.get_pos()
            mouse_botao = pygame.mouse.get_pressed()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # Desenha fundo e elementos do menu
            self.desenha_menu()
            self.__tela.display.blit(self.__logo_jogo, self.__logo_rect)
            self.__grupo_botoes.update()
            self.__grupo_botoes.draw(self.__tela.display)

            # Ações dos botões ao clicar
            if mouse_botao[0]:
                if botao_novojogo.rect.collidepoint(mouse_pos):
                    self.__som.tocar_efeitos(r"C:\GitHub\Jogo\sons\clique_inicio.wav")
                    self.__som.parar_musica()
                    self.__jogo.novo_jogo()
                    rodando_menu = False
                if botao_som.rect.collidepoint(mouse_pos):
                    self.__som.tocar_efeitos(r"C:\GitHub\Jogo\sons\clique.mp3")
                    self.menu_volume()

            pygame.display.update()
            self.clock.tick(60)
