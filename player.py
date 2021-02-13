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

# TODO - add speical squares
# 4 pointed star space - player gets another turn
# 6 pointed star space - player gets another turn??? player's piece on this space can't get removed from the board

class Player(pygame.sprite.Sprite):
    def __init__(self, mappings):
        super(Player, self).__init__()
        self.surf = pygame.Surface(const.BOARD_SQUARES_LOCATIONS[0][0])
        self.surf.fill(mappings['cursor_color'])
        self.rect = self.surf.get_rect(center = const.BOARD_SQUARES_LOCATIONS[0][0])
        self.row = 0
        self.col = 0
        self.color = mappings['color']
        self.keys = mappings['keys']
        self.move_seq = mappings['move_seq']
        self.pieces = []
        # self.selected_piece = None
        self.score = 0
        

    def draw(self, screen, turn):
        if turn:
            screen.blit(self.surf, self.rect)
        for piece in self.pieces:
            piece.draw(screen)
        

    def update(self, pressed_keys, last_pressed_keys):
        # always let player cursor move
        self.__move(pressed_keys, last_pressed_keys)

    def __move(self, pressed_keys, last_pressed_keys):
        if self.__hasKeyBeenPressed(pressed_keys, last_pressed_keys, self.keys['down']):
            self.__avoidMovingCursurOffBoard(self.keys['down'])
            self.row += 1     
        if self.__hasKeyBeenPressed(pressed_keys, last_pressed_keys, self.keys['up']):
            self.__avoidMovingCursurOffBoard(self.keys['up'])
            self.row -= 1    
        if self.__hasKeyBeenPressed(pressed_keys, last_pressed_keys, self.keys['right']):
            self.__avoidMovingCursurOffBoard(self.keys['right'])
            self.col += 1
        if self.__hasKeyBeenPressed(pressed_keys, last_pressed_keys, self.keys['left']):
            self.__avoidMovingCursurOffBoard(self.keys['left'])
            self.col -= 1
        self.__avoidOffScreenCursor()
        self.rect.center = const.BOARD_SQUARES_LOCATIONS[self.row][self.col]

    # checks if key has been press
    # only returns true when the key has been press after not being pressed 
    # ie. returns false if key is being held
    def __hasKeyBeenPressed(self, pressed_keys, last_pressed_keys, key):
        return pressed_keys[key] and last_pressed_keys[key] != pressed_keys[key]

    # adjust for the fact that the board has the 4 grey squares
    def __avoidMovingCursurOffBoard(self, direction):
        if self.col == 5 and (direction == self.keys['down'] or  direction == self.keys['up']):
            self.col += 1
        elif self.col == 4 and (direction == self.keys['down'] or direction == self.keys['up']):
            self.col -= 1
        if self.row != 1 and self.col == 6 and self.keys['left'] == direction:
            self.col -= 2
        if self.row != 1 and self.col == 3 and self.keys['right'] == direction:
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
    def addPieceToBoard(self, spaces_to_travel):
        self.pieces.append(Piece(self.color, self.move_seq[spaces_to_travel]))

    def getPieceAtLocation(self, point):
        for piece in self.pieces:
            if piece.xy_cord[0] == point[0] and piece.xy_cord[1] == point[1]:
                return piece
        return None

    def canPlayerMovePiece(self, piece, spaces_to_travel):
        if piece is not None:
            i = self.move_seq.index(piece.xy_cord)
            if i + spaces_to_travel < len(self.move_seq):
                p = self.getPieceAtLocation(self.move_seq[i + spaces_to_travel])
                return not self.getPieceAtLocation(self.move_seq[i + spaces_to_travel])
        return False

    def movePiece(self, piece, spaces_to_travel):
        if piece is not None:
            i = self.move_seq.index(piece.xy_cord)
            if i + spaces_to_travel < len(self.move_seq):
                piece.set_location(self.move_seq[i + spaces_to_travel])

    def hasAtLeastOneValidMove(self, spaces_to_travel):
        # first check if pieces on board can move
        for piece in self.pieces:
            if self.canPlayerMovePiece(piece, spaces_to_travel):
                return True
        # if pieces on board can't move then check if player can add a piece to the board
        if len(self.pieces) < const.TOTAL_NUM_OF_PLAYER_PIECES - self.score and not self.getPieceAtLocation(self.move_seq[spaces_to_travel - 1]):
            return True
        return False
