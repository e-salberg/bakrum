import pygame

class Piece(pygame.sprite.Sprite):
    def __init__(self, playerId,  color, xy):
        super(Piece, self).__init__()
        self.color = color
        self.xy_cord = xy
        self.playerId = playerId

    def moveToPoint(self, point):
        self.xy_cord = point 

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.xy_cord, 30)

