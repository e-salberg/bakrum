import pygame
import constants as const
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    KEYDOWN,
)

class Piece(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super(Piece, self).__init__()
        self.color = color
        self.row = x
        self.col = y


    def draw(self, screen):
        if self.row is not None and self.col is not None:
            pygame.draw.circle(screen, self.color, const.BOARD_SQUARES_LOCATIONS[self.row][self.col], 30)

    def set_location(self, row, col):
        if row is not None and row < len(const.BOARD_SQUARES_LOCATIONS):
            self.row = row
        if col is not None and col < len(const.BOARD_SQUARES_LOCATIONS[0]):
            self.col = col
