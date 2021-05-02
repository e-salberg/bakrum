import pytest
import bakrum.constants as const
from bakrum.piece import Piece

@pytest.fixture
def piece():
    return Piece(const.P1_MAPPINGS["id"], const.P1_MAPPINGS["color"], (75, 75))
 

def test_init(piece):
    assert piece.playerId == "p1"
    assert piece.color == const.WHITE 
    assert piece.xy_cord == (75, 75)

def test_moveToPoint(piece):
    piece.moveToPoint((100, 100))
    assert piece.xy_cord == (100, 100)