import pygame

class Piece(pygame.sprite.Sprite):
    def __init__(self, color, location):
        super(Piece, self).__init__()
        self.color = color
        self.location = location
        # TODO - add self.surf = piece image based on color?


    def draw(self, screen):
        # TODO - draw piece at self.location
        pygame.draw.circle(screen, (0, 0, 255), self.location, 75)