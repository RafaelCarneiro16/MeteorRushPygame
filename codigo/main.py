import pygame
import random
from jogador import Jogador
from tela import Tela
from menu import Menu
from jogo import Jogo
from som import Som


pygame.init()

tela = Tela(800, 600, 'C:/GitHub/Jogo/imagens/fundo.png')
tela_menu = Tela(800, 600, 'C:/GitHub/Jogo/imagens/fundo2.png')

# Grupos 
grupo_vidas = pygame.sprite.Group()
grupo_jogador = pygame.sprite.GroupSingle()
grupo_tiros = pygame.sprite.Group()
grupo_meteoros = pygame.sprite.Group()
grupo_botoes = pygame.sprite.Group()
grupo_meteoros_dourados = pygame.sprite.Group()

jogador = Jogador(grupo_jogador, tela)
grupo_sons = Som()

jogo = Jogo(tela, jogador, grupo_jogador, grupo_vidas, grupo_meteoros, grupo_tiros, grupo_sons, grupo_meteoros_dourados)

menu = Menu(jogo, tela_menu, grupo_botoes, grupo_sons)

while True:
    menu.rodando_menu()

    