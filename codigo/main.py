import pygame
import random
from jogador import Jogador
from tela import Tela
from tiro import Tiro
from meteoro import Meteoro
from vidas import Vidas
from menu import Menu
from jogo import Jogo


pygame.init()

tela = Tela(800, 600, 'C:/GitHub/MeteorRushPygame/imagens/fundo.png')

# Grupos 
grupo_vidas = pygame.sprite.Group()
grupo_jogador = pygame.sprite.GroupSingle()
grupo_tiros = pygame.sprite.Group()
grupo_meteoros = pygame.sprite.Group()
grupo_botoes = pygame.sprite.Group()

jogador = Jogador(grupo_jogador, tela)

jogo = Jogo(
    tela=tela,
    jogador=jogador,
    grupo_jogador=grupo_jogador,
    vidas=grupo_vidas,
    meteoro=grupo_meteoros,
    tiro=grupo_tiros
)

menu = Menu(jogo, tela, grupo_botoes)

while True:
    menu.rodando_menu()