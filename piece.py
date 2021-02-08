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
    def __init__(self, color, xy):
        super(Piece, self).__init__()
        self.color = color
        self.xy_cord = xy


    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.xy_cord, 30)

    def set_location(self, point):
        if point in const.PLAYER_SQUARES_SEQUENCE:
            self.xy_cord = point
        """if row is not None and row < len(const.BOARD_SQUARES_LOCATIONS):
            self.row = row
        if col is not None and col < len(const.BOARD_SQUARES_LOCATIONS[0]):
            self.col = col
            """
