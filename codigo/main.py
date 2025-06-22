import pygame
from jogador import Jogador
from tela import Tela
from menu import Menu
from jogo import Jogo
from som import Som
from gerenciador_raking import GerenciadorRanking  

pygame.init()

tela = Tela(800, 600, 'C:/GitHub/Jogo/imagens/fundo.png')
tela_menu = Tela(800, 600, 'C:/GitHub/Jogo/imagens/fundo2.png')

grupo_jogador = pygame.sprite.GroupSingle()

som = Som()
ranking = GerenciadorRanking()

jogador = Jogador(grupo_jogador, tela)

ranking.carregar_de_arquivo("ranking.json")

jogo = Jogo(tela, jogador, grupo_jogador, som)

menu = Menu(jogo, tela_menu, som, ranking)

while True:
    menu.rodando_menu()