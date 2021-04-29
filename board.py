import pygame
import constants as const
from piece import Piece
from player import Player

from pygame.locals import (
    RLEACCEL
)

class Board(pygame.sprite.Sprite):
    def __init__(self):
        super(Board, self).__init__()
        self.surf = pygame.image.load("./images/board.jpg").convert_alpha()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.p1 = Player(const.P1_MAPPINGS)
        self.p2 = Player(const.P2_MAPPINGS)
        self.pieces = []

    def addPieceToBoard(self, player, position):
        self.pieces.append(Piece(player.id, player.color, player.moveSeq[position]))

    def getPieceAtLocation(self, point):
        for piece in self.pieces:
            if piece.xy_cord[0] == point[0] and piece.xy_cord[1] == point[1]:
                return piece
        return None

    def movePiece(self, piece, spaces_to_travel):
        if piece is not None:
            moveSeq = self.getPieceSequenceOfMoves(piece)
            i = moveSeq.index(piece.xy_cord)
            if i + spaces_to_travel < len(moveSeq):
                piece.moveToPoint(moveSeq[i + spaces_to_travel])
    
    def removePiece(self, piece):
        self.pieces.remove(piece)

    def canPlayerMovePiece(self, player, piece, spaces_to_travel):
        if piece is not None and player.id == piece.playerId:
            moveSeq = self.getPieceSequenceOfMoves(piece)
            i = moveSeq.index(piece.xy_cord)
            if i + spaces_to_travel < len(moveSeq):
                pAtLocation = self.getPieceAtLocation(moveSeq[i + spaces_to_travel])
                return not (pAtLocation and pAtLocation.playerId == player.id)
        return False

    def hasAtLeastOneValidMove(self, player, spaces_to_travel):
        # first check if pieces on board can move
        for piece in self.pieces:
            if self.canPlayerMovePiece(player, piece, spaces_to_travel):
                return True
        # if pieces on board can't move then check if player can add a piece to the board
        pieceAtLocation = self.getPieceAtLocation(player.moveSeq[spaces_to_travel - 1])
        if self.numPlayerPiecesOnBoard(player) < const.TOTAL_NUM_OF_PLAYER_PIECES - player.score and not (pieceAtLocation is not None and pieceAtLocation.playerId == player.id):
            return True
        return False
    
    def numPlayerPiecesOnBoard(self, player):
        count = 0
        for piece in self.pieces:
            if piece.playerId == player.id:
                count += 1
        return count

    def getPieceSequenceOfMoves(self, piece):
        if piece.playerId == self.p1.id:
            return self.p1.moveSeq
        else: # piece.playerId == "p2"
            return self.p2.moveSeq
            
    def scorePoint(self, piece):
        if piece.playerId == self.p1.id:
           self.p1.score += 1
        else: # piece.playerId == self.p2.id:
            self.p2.score += 1
        self.pieces.remove(piece)

    def draw(self, screen, p1Turn):
        screen.blit(self.surf, self.rect)
        self.p1.draw(screen, p1Turn)
        self.p2.draw(screen, not p1Turn)
        for p in self.pieces:
            p.draw(screen)

    