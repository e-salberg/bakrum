import pygame
import constants as const
from player import Player
from board import Board

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

pygame.init()

# gameClock = pygame.time.Clock()

# draw screen
screen = pygame.display.set_mode([const.SCREEN_WIDTH, const.SCREEN_HEIGHT])

p1 = Player()
brd = Board()

done = False
while not done:

    # check if user exited the game
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                done = True
        elif event.type == QUIT:
            done = True

    # Get all the current pressed keys
    pressed_keys = pygame.key.get_pressed()
    p1.update(pressed_keys)

    # fill background with white
    screen.fill((0, 0, 0))
    
    # draw game board
    brd.draw(screen)

    #pygame.draw.circle(screen, (0, 0, 255), (785, 225), 30) 
    
    # draw player
    p1.draw(screen)

    # updates the contents of the display to the screen. Without this call, nothing appears in the window
    pygame.display.flip()

    #gameClock.tick(15)

pygame.quit()