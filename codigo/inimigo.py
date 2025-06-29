from abc import ABC, abstractmethod
import pygame

class Inimigo(pygame.sprite.Sprite, ABC):
    def __init__(self, grupo):
        super().__init__(grupo)

    @abstractmethod
    def update(self):
        pass
