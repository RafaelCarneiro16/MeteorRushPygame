import pygame
from jogo import Jogo
from menu import Menu

pygame.init()

jogo = Jogo()
menu = Menu(jogo)

while True:
    menu.rodando_menu()