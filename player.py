import pygame
import sys
import constants as const
from piece import Piece

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    K_RETURN,
    K_BACKSPACE,
    K_0,
    QUIT
)

class Player(pygame.sprite.Sprite):
    def __init__(self, color):
        super(Player, self).__init__()
        self.surf = pygame.Surface(const.BOARD_SQUARES_LOCATIONS[0][0])
        self.surf.fill(const.BLACK)
        self.rect = self.surf.get_rect(center = const.BOARD_SQUARES_LOCATIONS[0][0])
        self.row = 0
        self.col = 0
        self.color = color
        self.pieces = []
        self.selected_piece = None
        self.score = 0
        

    def draw(self, screen):
        screen.blit(self.surf, self.rect)
        for piece in self.pieces:
            piece.draw(screen)
        

    def update(self, pressed_keys, last_pressed_keys):
        # always let player cursor move
        self.__move(pressed_keys, last_pressed_keys)
        for p in self.pieces:
            if pressed_keys[K_RETURN] and p.row == self.row and p.col == self.col and self.selected_piece is None:
                # select piece at player's current position
                self.selected_piece = p
            elif pressed_keys[K_BACKSPACE] and self.selected_piece is not None:
                # deselect piece at player's current position
                self.selected_piece = None

        
        


    def __move(self, pressed_keys, last_pressed_keys):
        if self.__hasKeyBeenPressed(pressed_keys, last_pressed_keys, K_DOWN):
            self.__avoidMovingCursurOffBoard(K_DOWN)
            self.row += 1     
        if self.__hasKeyBeenPressed(pressed_keys, last_pressed_keys, K_UP):
            self.__avoidMovingCursurOffBoard(K_UP)
            self.row -= 1    
        if self.__hasKeyBeenPressed(pressed_keys, last_pressed_keys, K_RIGHT):
            self.__avoidMovingCursurOffBoard(K_RIGHT)
            self.col += 1
        if self.__hasKeyBeenPressed(pressed_keys, last_pressed_keys, K_LEFT):
            self.__avoidMovingCursurOffBoard(K_LEFT)
            self.col -= 1
        self.__avoidOffScreenCursor()
        self.rect.center = const.BOARD_SQUARES_LOCATIONS[self.row][self.col]
        # if there is a piece selected, update it's postion along with the player cursor
        if self.selected_piece:
            self.selected_piece.set_location(self.row, self.col)

    # checks if key has been press
    # only returns true when the key has been press after not being pressed 
    # ie. returns false if key is being held
    def __hasKeyBeenPressed(self, pressed_keys, last_pressed_keys, key):
        return pressed_keys[key] and last_pressed_keys[key] != pressed_keys[key]

    # adjust for the fact that the board has the 4 grey squares
    def __avoidMovingCursurOffBoard(self, direction):
        if self.col == 5 and (direction == K_DOWN or  direction == K_UP):
            self.col += 1
        elif self.col == 4 and (direction == K_DOWN or direction == K_UP):
            self.col -= 1
        if self.row != 1 and self.col == 6 and K_LEFT == direction:
            self.col -= 2
        if self.row != 1 and self.col == 3 and K_RIGHT == direction:
            self.col += 2

    def __avoidOffScreenCursor(self):
        if self.row >= len(const.BOARD_SQUARES_LOCATIONS):
            self.row = len(const.BOARD_SQUARES_LOCATIONS) - 1
        elif self.row < 0:
            self.row = 0
        if self.col >= len(const.BOARD_SQUARES_LOCATIONS[self.row]):
            self.col = len(const.BOARD_SQUARES_LOCATIONS[self.row]) - 1
        elif self.col < 0:
            self.col = 0

    # TODO - move this to game level instead of player level?
    # seems more like a game rule that player doesn't need to know when pieces are added to the board
    # player just needs to keep track of pieces once they are added
    # * maybe this is a public method but the check is at game level
    def addPieceToBoard(self):
        self.pieces.append(Piece(self.color, 0 , 3))

    def isPieceAtLocation(self, row, col):
        for piece in self.pieces:
            if row == piece.row and col == piece.col:
                return True
        return False