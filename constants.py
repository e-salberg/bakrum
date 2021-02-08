from enum import Enum

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    K_w,
    K_a,
    K_s,
    K_d,
    QUIT
)

# Color vector for white
WHITE = (255, 255, 255)

# Color vector for Black
BLACK = (0, 0 , 0)

# width of screen 
SCREEN_WIDTH = 1143

# height of screen 
SCREEN_HEIGHT = 437

# width of the board in px
BOARD_WIDTH = 1143

# height of the board in px
BOARD_HEIGHT = 437

# total number of pieces a player has
TOTAL_NUM_OF_PLAYER_PIECES = 7

# player one sequence of squares
PLAYER_SQUARES_SEQUENCE = [(500, 75), (360, 75), (215, 75), (75, 75), (75, 225), (215, 225), (360, 225), (500, 225), (642, 225), (785, 225), (925, 225), (1070, 225), (1070, 75), (925, 75), (780, 75)]

# squares only available to player 1
PLAYER_ONE_SQUARES = [(75, 75), (215, 75), (360, 75), (500, 75), (640, 75), (780, 75), (925, 75), (1070, 75)]

# squares available to both players
SHARED_SQUARES = [(75, 225), (215, 225), (360, 225), (500, 225), (642, 225), (785, 225), (925, 225), (1070, 225)]

# squares only available to player 2
PLAYER_TWO_SQUARES = [(75, 365), (215, 365), (360, 365), (500, 365), (640, 365), (780, 365), (925, 365), (1070, 365)]

BOARD_SQUARES_LOCATIONS = [PLAYER_ONE_SQUARES, SHARED_SQUARES, PLAYER_TWO_SQUARES]

# Player 1 key mappings
P1_KEY_MAPPINGS = {'left' : K_LEFT, 'right' : K_RIGHT, 'up' : K_UP, 'down' : K_DOWN}

# Player 2 key mappings
P2_KEY_MAPPINGS ={'left' : K_a, 'right' : K_d, 'up' : K_w, 'down' : K_s}

