import pygame
import random 
from jogador import Jogador
from tela import Tela
from tiro import Tiro
from meteoro import Meteoro


pygame.init()

clock = pygame.time.Clock()

tela = Tela(800,600)
imagem_fundo = pygame.image.load(rf"C:\jogotrab\imagens\fundo.png").convert_alpha()
rect_fundo = imagem_fundo.get_rect(center = (400,300))

sprites = pygame.sprite.Group()
jogador = Jogador(sprites, tela)

meteoros = pygame.sprite.Group()
tiros = pygame.sprite.Group()

evento_meteoro = pygame.USEREVENT + 1
pygame.time.set_timer(evento_meteoro, 250)

rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
           novo_tiro = Tiro((jogador.rect.midtop), tiros)

        if evento.type == evento_meteoro:
            x = random.randint(0, tela.largura - 50)
            novo_meteoro = Meteoro(x , meteoros)   
    
    pygame.sprite.groupcollide(tiros, meteoros, True, True, pygame.sprite.collide_rect)
    pygame.sprite.groupcollide(sprites, meteoros, False, True, pygame.sprite.collide_rect)


    tela.display.fill('midnightblue')
    tela.display.blit(imagem_fundo , rect_fundo)

    sprites.update(tela)
    tiros.update()
    meteoros.update()

    sprites.draw(tela.display)
    tiros.draw(tela.display)
    meteoros.draw(tela.display)

    pygame.display.update()
    clock.tick(60)

pygame.quit()