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

# RGB value for white
WHITE = (255, 255, 255)

# RGB value for Black
BLACK = (0, 0 , 0)

# RGB value for Blue
BLUE = (0, 0, 255)

# RGB value for Grey
GREY = (140, 140, 140)

# RGB value off-white
OFF_WHITE = (220, 220, 220)

# RGB value off-black
OFF_BLACK = (54, 54, 54)

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

# min spaces a piece can move in one turn
MIN_MOVE = 0

# max spaces a piece can move in one turn
MAX_MOVE = 4

# location of player score
# PLAYER_SCORE_CENTER = (640, 75)

# player one sequence of squares
PLAYER_ONE_SQUARES_SEQUENCE = [(500, 75), (360, 75), (215, 75), (75, 75), (75, 225), (215, 225), (360, 225), (500, 225), (642, 225), (785, 225), (925, 225), (1070, 225), (1070, 75), (925, 75), (780, 75)]

# player two sequence of squares
PLAYER_TWO_SQUARES_SEQUENCE = [(500, 365), (360, 365), (215, 365), (75, 365), (75, 225), (215, 225), (360, 225), (500, 225), (642, 225), (785, 225), (925, 225), (1070, 225), (1070, 365), (925, 365), (780, 365)]

# squares only available to player 1
PLAYER_ONE_SQUARES = [(75, 75), (215, 75), (360, 75), (500, 75), (640, 75), (780, 75), (925, 75), (1070, 75)]

# squares available to both players
SHARED_SQUARES = [(75, 225), (215, 225), (360, 225), (500, 225), (642, 225), (785, 225), (925, 225), (1070, 225)]

# squares only available to player 2
PLAYER_TWO_SQUARES = [(75, 365), (215, 365), (360, 365), (500, 365), (640, 365), (780, 365), (925, 365), (1070, 365)]

BOARD_SQUARES_LOCATIONS = [PLAYER_ONE_SQUARES, SHARED_SQUARES, PLAYER_TWO_SQUARES]

KEEP_TURN_SQUARES = [BOARD_SQUARES_LOCATIONS[0][0], BOARD_SQUARES_LOCATIONS[2][0], BOARD_SQUARES_LOCATIONS[0][6], BOARD_SQUARES_LOCATIONS[2][6]] 

# Player 1 mappings
P1_MAPPINGS = {'color' : WHITE, 'cursor_color' : OFF_BLACK, 'move_seq' : PLAYER_ONE_SQUARES_SEQUENCE, 'score_center' : (640, 75), 'keys' : {'left' : K_a, 'right' : K_d, 'up' : K_w, 'down' : K_s}}

# Player 2 key mappings
P2_MAPPINGS = {'color' : BLACK, 'cursor_color' : OFF_WHITE, 'move_seq' : PLAYER_TWO_SQUARES_SEQUENCE, 'score_center' : (780, 75), 'keys' : {'left' : K_a, 'right' : K_d, 'up' : K_w, 'down' : K_s}}

