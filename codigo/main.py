import pygame
from jogo import Jogo
from menu import Menu
from som import Som

pygame.init()

som = Som()
jogo = Jogo(som)
menu = Menu(jogo,som)

while True:
    menu.rodando_menu()