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
from explosao import Explosao
from powerups import PowerUp
from ovni import Ovni

class Jogo():
    def __init__(self):
        self.__tela = Tela(800, 600, r'C:/GitHub/Jogo/imagens/fundo.png')
        self.__grupo_jogador = pygame.sprite.GroupSingle()
        self.__jogador = Jogador(self.__grupo_jogador, self.__tela)
        self.__grupo_vidas = pygame.sprite.Group()
        self.__grupo_meteoros = pygame.sprite.Group()
        self.__grupo_tiros = pygame.sprite.Group()
        self.__clock = pygame.time.Clock()
        self.__som = Som()
        self.__grupo_meteoros_dourados = pygame.sprite.Group()
        self.__ranking = GerenciadorRanking()
        self.__ranking.carregar_de_arquivo("ranking.json")
        self.__cenario = Cenario(self.__tela)
        self.__grupo_explosoes = pygame.sprite.Group()
        self.__grupo_powerup = pygame.sprite.Group()
        self.__grupo_pause = pygame.sprite.GroupSingle()
        self.__botao_pause = Botao(self.grupo_pause, r'C:\GitHub\Jogo\imagens\pause.png', (60, 560))
        self.__lista_vidas = []
        self.__pontuacao = 0
        self.__grupo_ovnis = pygame.sprite.Group()
        self.__grupo_tiros_inimigos = pygame.sprite.Group()
        self.ovni_ativo = False
        self.evento_ovni = pygame.USEREVENT + 3

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

    @property
    def grupo_explosoes(self):
        return self.__grupo_explosoes

    @grupo_explosoes.setter
    def grupo_explosoes(self, value):
        self.__grupo_explosoes = value

    @property
    def grupo_powerup(self):
        return self.__grupo_powerup

    @grupo_powerup.setter
    def grupo_powerup(self, value):
        self.__grupo_powerup = value

    @property
    def grupo_pause(self):
        return self.__grupo_pause

    @grupo_pause.setter
    def grupo_pause(self, value):
        self.__grupo_pause = value

    @property
    def botao_pause(self):
        return self.__botao_pause

    @botao_pause.setter
    def botao_pause(self, value):
        self.__botao_pause = value

    @property
    def lista_vidas(self):
        return self.__lista_vidas

    @lista_vidas.setter
    def lista_vidas(self, value):
        self.__lista_vidas = value

    @property
    def pontuacao(self):
        return self.__pontuacao

    @pontuacao.setter
    def pontuacao(self, value):
        self.__pontuacao = value

    @property
    def ranking(self):
        return self.__ranking

    @ranking.setter
    def ranking(self, value):
        self.__ranking = value    
    @property
    def grupo_ovnis(self):
        return self.__grupo_ovnis

    @grupo_ovnis.setter
    def grupo_ovnis(self, value):
        self.__grupo_ovnis = value

    @property
    def grupo_tiros_inimigos(self):
        return self.__grupo_tiros_inimigos

    @grupo_tiros_inimigos.setter
    def grupo_tiros_inimigos(self, value):
        self.__grupo_tiros_inimigos = value


    #endregion

    def novo_jogo(self):
        self.grupo_meteoros.empty()
        self.grupo_meteoros_dourados.empty()
        self.grupo_powerup.empty()
        self.grupo_tiros.empty()
        self.jogador.rect.center = (400,400)
        self.lista_vidas = []
        self.pontuacao = 0
        self.jogador.tiro_triplo = False
        self.grupo_meteoros_dourados.empty()
        self.grupo_ovnis.empty()
        self.grupo_tiros_inimigos.empty()
            
        for i in range(3):
            x = self.tela.largura - (i * (40+5))
            vida = Vidas(self.grupo_vidas, x)
            self.lista_vidas.append(vida)

    
        font = pygame.font.Font(r'C:\GitHub\Jogo\fonte.ttf', 24)

        evento_meteoro = pygame.USEREVENT + 1
        evento_meteoro_dourado = pygame.USEREVENT + 2
        pygame.time.set_timer(evento_meteoro, 250)
        pygame.time.set_timer(evento_meteoro_dourado, 2000)
        pygame.time.set_timer(self.evento_ovni, 1000, loops=1)

        rodando = True
        self.som.tocar_musica(rf"C:\GitHub\Jogo\sons\musica_jogo.wav")

        while rodando:
            self.testes_evento(evento_meteoro, evento_meteoro_dourado)
            mouse_pos = pygame.mouse.get_pos()
            mouse_botao = pygame.mouse.get_pressed()

            if mouse_botao[0]:
                if self.botao_pause.rect.collidepoint(mouse_pos):
                    resultado = self.pause()
                    if not resultado:
                        return

            resultadocolisoes = self.colisoes()
            if resultadocolisoes:
                return

            self.pontuacao = self.colisao_meteoro(self.grupo_tiros, self.grupo_meteoros, self.pontuacao, False)
            self.pontuacao = self.colisao_meteoro(self.grupo_tiros, self.grupo_meteoros_dourados, self.pontuacao, True)

            # Atualizações dos grupos
            self.updates()
            
            # Atualizar e desenhar o fundo animado
            self.tela.fundo_mover()

            # Atualizar e desenhar o cenário 
            self.cenario.update()
            self.cenario.draw(self.tela.display)

            # Desenhos
            self.desenhos()
            escudo_ativo = next((p for p in self.grupo_powerup if p.tipo == 'escudo'), None)
            tiro_triplo_ativo = next((p for p in self.grupo_powerup if p.tipo == 'tiro_triplo'), None)
            
            if escudo_ativo:
                escudo_ativo.desenhar_temporizador()
            if tiro_triplo_ativo:
                tiro_triplo_ativo.desenhar_temporizador()    

          
            texto_pontuacao = font.render(f"Pontuação: {self.pontuacao}", True, (255, 255, 255))
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

    def game_over(self, pontuacao): 
        grupo_botoes = pygame.sprite.Group()
        pausado = True
        botao_game_over = Botao(grupo_botoes, rf'C:\GitHub\Jogo\imagens\titulo_game_over.png', (400, 120))
        botao_novo_jogo = Botao(grupo_botoes, rf'C:\GitHub\Jogo\imagens\bt_novo_jogo.png', (400, 260))
        botao_menu = Botao(grupo_botoes, rf'C:\GitHub\Jogo\imagens\bt_menu_principal.png', (400, 380))
        botao_sair = Botao(grupo_botoes, rf'C:\GitHub\Jogo\imagens\bt_salvar_sair.png', (400, 500))

        nome = self.ranking.solicitar_nome(self.__tela, self.__clock, botao_game_over)
        self.ranking.adicionar_jogador(JogadorRanking(nome, pontuacao)) 
        self.ranking.salvar_em_arquivo("ranking.json")
      
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
                elif botao_novo_jogo.rect.collidepoint(mouse_pos):
                    self.som.tocar_efeitos(r"C:\GitHub\Jogo\sons\clique.mp3")
                    self.novo_jogo()
                    return
                elif botao_sair.rect.collidepoint(mouse_pos):
                    self.som.tocar_efeitos(r"C:\GitHub\Jogo\sons\clique.mp3")
                    pygame.quit()
                    exit()

            self.tela.display.blit(self.tela.imagem_fundo, (0,0))
            grupo_botoes.update()
            grupo_botoes.draw(self.tela.display)

            pygame.display.update()
            self.clock.tick(15)

    def colisao_meteoro(self, grupo_tiros , grupo_meteoros, pontuacao, power_up: bool): 
        colisao = pygame.sprite.groupcollide(grupo_tiros, grupo_meteoros, True, True)
        for tiros, meteoros_acertados in colisao.items():
            for meteoro in meteoros_acertados:
                pontuacao += meteoro.pontos
                self.som.tocar_efeitos(r"C:\GitHub\Jogo\sons\explosion.wav")
                Explosao(self.grupo_explosoes, self.tela, meteoro.rect.center)
                if power_up and random.random() <= 0.3:
                      PowerUp('power_up', self.grupo_powerup, meteoro.rect.center, self.tela, self.jogador)
        
        return pontuacao
    
    def testes_evento(self, evento_meteoro, evento_meteoro_dourado): 
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return
                elif evento.key == pygame.K_SPACE:
                    if not self.jogador.tiro_triplo:
                        Tiro((self.jogador.rect.midtop), self.grupo_tiros, direcao = 1, caminho_imagem = rf'C:\GitHub\Jogo\imagens\tiro_jogador.png')
                        self.som.tocar_efeitos(rf"C:\GitHub\Jogo\sons\laser.wav")

                    else:
                        x, y = self.jogador.rect.midtop
                        Tiro((x - 20, y), self.grupo_tiros, direcao = 1, caminho_imagem = rf'C:\GitHub\Jogo\imagens\tiro_jogador.png')
                        Tiro((x, y - 20), self.grupo_tiros, direcao = 1, caminho_imagem = rf'C:\GitHub\Jogo\imagens\tiro_jogador.png')
                        Tiro((x + 20, y), self.grupo_tiros, direcao = 1, caminho_imagem =rf'C:\GitHub\Jogo\imagens\tiro_jogador.png')
                        self.som.tocar_efeitos(rf"C:\GitHub\Jogo\sons\laser.wav")
                        
            elif evento.type == evento_meteoro:
                x = random.randint(0, self.tela.largura - 50)
                Meteoro(x, self.grupo_meteoros)

            elif evento.type == evento_meteoro_dourado:
                x = random.randint(0, self.tela.largura - 50)
                Meteoro_Dourado(self.grupo_meteoros_dourados, self.tela ,self.jogador)
            
            elif evento.type == self.evento_ovni and not self.ovni_ativo:
                Ovni(self.grupo_ovnis, rf"C:\GitHub\Jogo\imagens\ovni.png", (random.randint(100, 700), 100), self.grupo_tiros_inimigos, self.jogador)
                self.ovni_ativo = True

    def colisoes(self):
        colisao_ovnis = pygame.sprite.groupcollide(self.grupo_tiros, self.grupo_ovnis, True, True)
        for tiros, ovnis_acertados in colisao_ovnis.items():
            for ovni in ovnis_acertados:
                self.som.tocar_efeitos(r"C:\GitHub\Jogo\sons\explosion.wav")
                Explosao(self.grupo_explosoes, self.tela, ovni.rect.center)
                self.ovni_ativo = False
                pygame.time.set_timer(self.evento_ovni, 8000, loops=1) 

        colisao_powerup = pygame.sprite.spritecollide(self.jogador, self.grupo_powerup, False)
        for powerup in colisao_powerup:
            if powerup.tipo == 'power_up':
                powerup.kill()
                powerup_ativo = any(p.tipo in ['escudo', 'tiro_triplo'] for p in self.grupo_powerup)
                
                if not powerup_ativo:
                    self.som.tocar_efeitos(r"C:\GitHub\Jogo\sons\power_up.wav")
                    escolhido = random.choice(['escudo', 'tiro_triplo'])
                    PowerUp(escolhido, self.grupo_powerup, self.jogador.rect.center, self.tela, self.jogador)

        escudo_ativo = next((p for p in self.grupo_powerup if p.tipo == 'escudo'), None)

        if escudo_ativo:
            pygame.sprite.spritecollide(escudo_ativo, self.grupo_meteoros, True)
            pygame.sprite.spritecollide(escudo_ativo, self.grupo_meteoros_dourados, True)
            pygame.sprite.spritecollide(escudo_ativo, self.grupo_tiros_inimigos, True)

        else:
            colisao_jogador_m = pygame.sprite.spritecollide(self.jogador, self.grupo_meteoros, True)
            colisao_jogador_md = pygame.sprite.spritecollide(self.jogador, self.grupo_meteoros_dourados, True)
            colisao_tiro_jogador = pygame.sprite.spritecollide(self.jogador, self.grupo_tiros_inimigos, True)

            if colisao_jogador_m or colisao_jogador_md:
                self.som.tocar_efeitos(r"C:\GitHub\Jogo\sons\hit.wav")
                if self.lista_vidas:
                    vida_perdida = self.lista_vidas.pop()
                    vida_perdida.kill()
                    if not self.lista_vidas:
                        self.som.parar_musica()
                        self.som.tocar_efeitos(r"C:\GitHub\Jogo\sons\game_over_efeito.wav")
                        self.game_over(self.pontuacao)
                        return True

            for tiro in colisao_tiro_jogador:
                self.som.tocar_efeitos(r"C:\GitHub\Jogo\sons\hit.wav")
                if self.lista_vidas:
                    vida_perdida = self.lista_vidas.pop()
                    vida_perdida.kill()
                    if not self.lista_vidas:
                        self.som.parar_musica()
                        self.som.tocar_efeitos(r"C:\GitHub\Jogo\sons\game_over_efeito.wav")
                        self.game_over(self.pontuacao)
                        return True        
                        
    def updates(self):
        self.grupo_jogador.update()
        self.grupo_tiros.update()
        self.grupo_meteoros.update()
        self.grupo_vidas.update()
        self.grupo_meteoros_dourados.update()
        self.grupo_explosoes.update()
        self.grupo_powerup.update()
        self.grupo_pause.update()
        self.grupo_ovnis.update()
        self.grupo_tiros_inimigos.update()

    def desenhos(self):
        self.grupo_jogador.draw(self.tela.display)
        self.jogador.animacao_vento()
        self.grupo_tiros.draw(self.tela.display)
        self.grupo_meteoros.draw(self.tela.display)
        self.grupo_vidas.draw(self.tela.display)
        self.grupo_meteoros_dourados.draw(self.tela.display)        
        self.grupo_explosoes.draw(self.tela.display)
        self.grupo_powerup.draw(self.tela.display)
        self.grupo_pause.draw(self.tela.display)
        self.grupo_ovnis.draw(self.tela.display)
        self.grupo_tiros_inimigos.draw(self.tela.display)