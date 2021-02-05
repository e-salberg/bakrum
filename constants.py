from enum import Enum

class Color(Enum):
    BLACK = 0
    WHITE = 1

# width of screen 
SCREEN_WIDTH = 1143

# height of screen 
SCREEN_HEIGHT = 437

# width of the board in px
BOARD_WIDTH = 1143

# height of the board in px
BOARD_HEIGHT = 437

# squares only available to player 1
PLAYER_ONE_SQUARES = [(75, 75), (215, 75), (360, 75), (500, 75), (640, 75), (780, 75), (925, 75), (1070, 75)]

# squares available to both players
SHARED_SQUARES = [(75, 225), (215, 225), (360, 225), (500, 225), (642, 225), (785, 225), (925, 225), (1070, 225)]

# squares only available to player 2
PLAYER_TWO_SQUARES = [(75, 365), (215, 365), (360, 365), (500, 365), (640, 365), (780, 365), (925, 365), (1070, 365)]

BOARD_SQUARES_LOCATIONS = [PLAYER_ONE_SQUARES, SHARED_SQUARES, PLAYER_TWO_SQUARES]

"""
# Squares but as dicts with keys x, y
# not sure if these make code easier to read???
# squares only available to player 1 
PLAYER_ONE_SQUARES = [{'x' : 75, 'y' : 75}, {'x' : 215, 'y' : 75}, {'x' : 360, 'y' : 75}, {'x' : 500, 'y' : 75}, {'x' : 925, 'y' : 75}, {'x' : 1070, 'y' : 75}]

#squares available to both players
SHARED_SQUARES = [{'x' : 75, 'y' : 225}, {'x' : 215, 'y' : 225}, {'x' : 360, 'y' : 225}, {'x' : 500, 'y' : 225}, {'x' : 642, 'y': 225}, {'x' : 785, 'y' : 225}, {'x' : 925, 'y' : 225}, {'x' : 1070, 'y' : 225}]

#squares only available to player 2
PLAYER_TWO_SQUARES = [{'x' : 75, 'y' : 365}, {'x' : 215, 'y' : 365}, {'x' : 360, 'y' : 365}, {'x' : 500, 'y' : 365}, {'x' : 925, 'y' : 365}, {'x' : 1070, 'y' : 365}]

#representation of the board
BOARD_SQUARES_LOCATIONS = [PLAYER_ONE_SQUARES, SHARED_SQUARES, PLAYER_TWO_SQUARES]
"""
