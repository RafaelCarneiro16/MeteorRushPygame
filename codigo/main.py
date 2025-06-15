import pygame
import random
from jogador import Jogador
from tela import Tela
from tiro import Tiro
from meteoro import Meteoro
from vidas import Vidas
from menu import Menu
from jogo import Jogo
from som import Som


pygame.init()

tela = Tela(800, 600, 'C:/GitHub/Jogo/imagens/fundo.png')

# Grupos 
grupo_vidas = pygame.sprite.Group()
grupo_jogador = pygame.sprite.GroupSingle()
grupo_tiros = pygame.sprite.Group()
grupo_meteoros = pygame.sprite.Group()
grupo_botoes = pygame.sprite.Group()
jogador = Jogador(grupo_jogador, tela)
grupo_sons = Som()

jogo = Jogo(
    tela=tela,
    jogador=jogador,
    grupo_jogador=grupo_jogador,
    vidas=grupo_vidas,
    meteoro=grupo_meteoros,
    tiro=grupo_tiros,
    som=grupo_sons
)

menu = Menu(jogo, tela, grupo_botoes)

while True:
    menu.rodando_menu()

    