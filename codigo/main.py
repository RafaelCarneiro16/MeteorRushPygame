import pygame
import random
from jogador import Jogador
from tela import Tela
from tiro import Tiro
from meteoro import Meteoro
from vidas import Vidas

pygame.init()

tela = Tela(800,600)

clock = pygame.time.Clock()

def menu():
    rodando_menu = True

    imagem_fundo = pygame.image.load(rf"C:\GitHub\Jogo\imagens\fundo.png").convert_alpha()
    rect_fundo = imagem_fundo.get_rect(center = (400,300))

    font = pygame.font.SysFont(None, 36)
    texto = font.render(f"Menu Principal", True, (255, 255, 255))
    texto_rect = texto.get_rect(center = (400,75))
    tela.display.blit(imagem_fundo, rect_fundo)
    tela.display.blit(texto, texto_rect)

    while rodando_menu:

        mouse_menu = pygame.mouse.get_pos()

        for evento in pygame.event.get():
           if evento.type == pygame.QUIT:
              pygame.quit()
              exit()

           if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:     
               novo_jogo()
               rodando_menu = False
    
        pygame.display.update()
clock.tick(60)

# Loop do Jogo
def novo_jogo():
    
    coracoes = pygame.sprite.Group()
    lista_vidas = []
    
    for i in range(3):
       x = tela.largura - (i * (50 + 10))
       vida = Vidas(coracoes, x)
       lista_vidas.append(vida)


    pontuacao = 0 
    font = pygame.font.SysFont(None, 36)
    
    jogador_sprite = pygame.sprite.Group()
    jogador = Jogador(jogador_sprite, tela)

    meteoros = pygame.sprite.Group()
    tiros = pygame.sprite.Group()

    evento_meteoro = pygame.USEREVENT + 1
    pygame.time.set_timer(evento_meteoro, 250)
    
    imagem_fundo = pygame.image.load(rf"C:\GitHub\Jogo\imagens\fundo.png").convert_alpha()
    rect_fundo = imagem_fundo.get_rect(center = (400,300))

    rodando = True

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif evento.type == pygame.KEYDOWN :
                # Cria tiro
                if evento.key == pygame.K_SPACE:
                    novo_tiro = Tiro((jogador.rect.midtop), tiros)
                # Volta pro menu
                if evento.key == pygame.K_ESCAPE:
                    return 

            # Gera meteoros
            elif evento.type == evento_meteoro:
                x = random.randint(0, tela.largura - 50)
                novo_meteoro = Meteoro(x , meteoros)   

        # Colisão

        colisao_jogador = pygame.sprite.spritecollide(jogador, meteoros, True)

        if colisao_jogador:
           if lista_vidas:
              vida_perdida = lista_vidas.pop()
              vida_perdida.kill()
           else:
              rodando = False 

        colisao = pygame.sprite.groupcollide(tiros, meteoros, True, True)

        for tiro, meteoros_acert in colisao.items():
            for meteoro in meteoros_acert:
                pontuacao+= meteoro.pontos
   

        # Atualização da posição
        jogador_sprite.update(tela)
        tiros.update()
        meteoros.update()
        coracoes.update()
        
        # Desenhos
        tela.display.blit(imagem_fundo , rect_fundo)
        jogador_sprite.draw(tela.display)
        tiros.draw(tela.display)
        meteoros.draw(tela.display)
        coracoes.draw(tela.display)

        texto_pontuacao = font.render(f"Pontuação: {pontuacao}", True, (255, 255, 255))
        tela.display.blit(texto_pontuacao, (10, 10))

        pygame.display.update()
        clock.tick(60)

while True:
    menu()

pygame.quit()