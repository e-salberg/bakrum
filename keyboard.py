import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

def update(player, pressed_keys):
    
    """
    if pressed_keys[K_UP]:
        player.rect.move_ip(0, -5)
    elif pressed_keys[K_DOWN]:
        player.rect.move_ip(0, 5)
    elif pressed_keys[K_LEFT]:
        player.rect.move_ip(-5, 0)
    elif pressed_keys[K_RIGHT]:
        player.rect.move_ip(5, 0)
    """        