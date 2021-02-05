import pygame
from constants import Color
import constants as const

from pygame.locals import (
    RLEACCEL
)

class Board(pygame.sprite.Sprite):
    def __init__(self):
        super(Board, self).__init__()
        self.surf = pygame.image.load("./images/board.jpg").convert_alpha()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

        # list of all spots [(x1,y1), (x2,y2) ...]
        # list of all pieces of board 

    

    def draw(self, screen):
        screen.blit(self.surf, self.rect)
