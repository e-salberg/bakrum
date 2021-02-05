import pygame
import sys
import constants as const

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface(const.BOARD_SQUARES_LOCATIONS[0][0])
        self.surf.fill((0, 0, 255))
        self.rect = self.surf.get_rect(center = const.BOARD_SQUARES_LOCATIONS[0][0])
        self.row = 0
        self.col = 0
        self.last_pressed_keys = pygame.key.get_pressed()
        # TODO add list to hold players pieces?
        

    def draw(self, screen):
        screen.blit(self.surf, self.rect)

    def update(self, pressed_keys):
        if pressed_keys[K_DOWN] and self.last_pressed_keys[K_DOWN] != pressed_keys[K_DOWN]:        
            self.__avoidMovingOffBoard(K_DOWN)
            self.row += 1          
        if pressed_keys[K_UP] and self.last_pressed_keys[K_UP] != pressed_keys[K_UP]:
            self.__avoidMovingOffBoard(K_UP)
            self.row -= 1         
        if pressed_keys[K_RIGHT] and self.last_pressed_keys[K_RIGHT] != pressed_keys[K_RIGHT]:
            self.__avoidMovingOffBoard(K_RIGHT)
            self.col += 1
        if pressed_keys[K_LEFT] and self.last_pressed_keys[K_LEFT] != pressed_keys[K_LEFT]:
            self.__avoidMovingOffBoard(K_LEFT)
            self.col -= 1
        self.__avoidOffScreenPoints()
        self.rect.center = const.BOARD_SQUARES_LOCATIONS[self.row][self.col]    
        self.last_pressed_keys = pressed_keys


    # adjust for the fact that the board has the 4 grey squares
    def __avoidMovingOffBoard(self, direction):
        if self.col == 5 and (direction == K_DOWN or  direction == K_UP):
            self.col += 1
        elif self.col == 4 and (direction == K_DOWN or direction == K_UP):
            self.col -= 1
        if self.row != 1 and self.col == 6 and K_LEFT == direction:
            self.col -= 2
        if self.row != 1 and self.col == 3 and K_RIGHT == direction:
            self.col += 2

    def __avoidOffScreenPoints(self):
        if self.row >= len(const.BOARD_SQUARES_LOCATIONS):
            self.row = len(const.BOARD_SQUARES_LOCATIONS) - 1
        elif self.row < 0:
            self.row = 0
        if self.col >= len(const.BOARD_SQUARES_LOCATIONS[self.row]):
            self.col = len(const.BOARD_SQUARES_LOCATIONS[self.row]) - 1
        elif self.col < 0:
            self.col = 0
