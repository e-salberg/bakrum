import pytest
import bakrum.constants as const
from bakrum.player import Player

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

@pytest.fixture
def player():
    return Player(const.P1_MAPPINGS)

def test_init(player):
    assert player.color == const.WHITE
    assert player.score == 0
    assert player.id == const.P1_MAPPINGS["id"]
    assert player.row == 0
    assert player.col == 0

def test_scorePoint(player):
    start_score = player.score
    player.scorePoint()
    assert player.score == start_score + 1

def test_avoidOffScreenCursorGreater(player):
    player.row = len(const.BOARD_SQUARES_LOCATIONS)
    player.col = len(const.BOARD_SQUARES_LOCATIONS[player.row - 1])
    player._Player__avoidOffScreenCursor()
    assert player.row == len(const.BOARD_SQUARES_LOCATIONS) - 1
    assert player.col == len(const.BOARD_SQUARES_LOCATIONS[player.row]) - 1

def test_avoidOffScreenCursor0(player):
    player.row = -1
    player.col = -1
    player._Player__avoidOffScreenCursor()
    assert player.row == 0
    assert player.col == 0

def test_avoidMovingCursurOffBoardUp(player):
    player.col = 5
    direct = const.P1_MAPPINGS["keys"]["up"]
    player._Player__avoidMovingCursurOffBoard(direct)
    assert player.col == 6

def test_avoidMovingCursurOffBoardRight(player):
    player.col = 3
    direct = const.P1_MAPPINGS["keys"]["right"]
    player._Player__avoidMovingCursurOffBoard(direct)
    assert player.col == 5

def test_avoidMovingCursurOffBoardDown(player):
    player.col = 4
    direct = const.P1_MAPPINGS["keys"]["down"]
    player._Player__avoidMovingCursurOffBoard(direct)
    assert player.col == 3

def test_avoidMovingCursurOffBoardLeft(player):
    player.col = 6
    direct = const.P1_MAPPINGS["keys"]["left"]
    player._Player__avoidMovingCursurOffBoard(direct)
    assert player.col == 4

def test_hasKeyBeenPressedTrue(player):
    key = "test_key"
    pressedKeys = {"test_key" : True}
    lastPressed = {"test_key" : False}
    result = player._Player__hasKeyBeenPressed(pressedKeys, lastPressed, key)
    assert result == True

def test_hasKeyBeenPressedFalse(player):
    key = "test_key"
    pressedKeys = {"test_key" : False}
    lastPressed = {"test_key" : False}
    result = player._Player__hasKeyBeenPressed(pressedKeys, lastPressed, key)
    assert result == False

def test_hasKeyBeenPressedKeyBeingHeld(player):
    key = "test_key"
    pressedKeys = {"test_key" : True}
    lastPressed = {"test_key" : True}
    result = player._Player__hasKeyBeenPressed(pressedKeys, lastPressed, key)
    assert result == False

def test_moveRight(player):
    prev_row = player.row
    prev_col = player.col
    # right left up down
    pressedKeys = {100 : True, 97 : False, 119 : False, 115 : False}
    lastPressed = {100 : False, 97 : False, 119 : False, 115 : False}
    player._Player__move(pressedKeys, lastPressed)
    assert prev_row == player.row
    assert prev_col + 1 == player.col

def test_moveLeft(player):
    player.col = 1
    prev_row = player.row
    prev_col = player.col
    # right left up down
    pressedKeys = {100 : False, 97 : True, 119 : False, 115 : False}
    lastPressed = {100 : False, 97 : False, 119 : False, 115 : False}
    player._Player__move(pressedKeys, lastPressed)
    assert prev_row == player.row
    assert prev_col - 1 == player.col

def test_moveUp(player):
    player.row = 1
    prev_row = player.row
    prev_col = player.col
    # right left up down
    pressedKeys = {100 : False, 97 : False, 119 : True, 115 : False}
    lastPressed = {100 : False, 97 : False, 119 : False, 115 : False}
    player._Player__move(pressedKeys, lastPressed)
    assert prev_row - 1 == player.row
    assert prev_col == player.col

def test_moveDown(player):
    prev_row = player.row
    prev_col = player.col
    # right left up down
    pressedKeys = {100 : False, 97 : False, 119 : False, 115 : True}
    lastPressed = {100 : False, 97 : False, 119 : False, 115 : False}
    player._Player__move(pressedKeys, lastPressed)
    assert prev_row + 1 == player.row
    assert prev_col == player.col
