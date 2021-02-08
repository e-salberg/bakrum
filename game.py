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
    K_0,
    K_RETURN,
    QUIT
)


def main():
    pygame.init()

    # draw screen
    screen = pygame.display.set_mode([const.SCREEN_WIDTH, const.SCREEN_HEIGHT])

    p1 = Player(const.WHITE)
    brd = Board()

    font = pygame.font.Font('freesansbold.ttf', 50)

    # create a text suface object,
    # on which text is drawn on it.
    text = font.render('0', True, (0, 0, 255))

    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()
    textRect.center = (640, 75)

    # keep track of keys pressed last frame to prevent keys held down from triggering events
    last_pressed_keys = pygame.key.get_pressed()

    done = False
    while not done:

        # check if user exited the game
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    done = True
            # if user closed the game window
            elif event.type == QUIT:
                done = True

        # Get all the current pressed keys and process results
        pressed_keys = pygame.key.get_pressed()
        if __hasKeyBeenPressed(pressed_keys, last_pressed_keys, K_0):
            addPieceToBoard(p1)
        if __hasKeyBeenPressed(pressed_keys, last_pressed_keys, K_RETURN):
            piece = p1.getPieceAtLocation(const.BOARD_SQUARES_LOCATIONS[p1.row][p1.col])
            if p1.canPlayerMovePiece(piece):
                p1.movePiece(piece)


        p1.update(pressed_keys, last_pressed_keys)

        scoredPiece = pieceReachedGoal(p1)
        if scoredPiece is not None: # and scoredPiece is not p1.selected_piece:
            scorePoint(p1, scoredPiece)
            text = font.render(str(p1.score), True, (0, 0, 255))

        # fill background with white
        screen.fill((0, 0, 0))

        # draw game board
        brd.draw(screen)

        # draw player
        p1.draw(screen)

        # draw text
        screen.blit(text, textRect)

        # updates the contents of the display to the screen. Without this call, nothing appears in the window
        pygame.display.flip()

        # keep track of keys pressed last frame to prevent keys held down from triggering events
        last_pressed_keys = pygame.key.get_pressed()

    pygame.quit()


def pieceReachedGoal(player):
    result = None
    for piece in player.pieces:
        # piece_location = const.BOARD_SQUARES_LOCATIONS[piece.row][piece.col]
        if piece.xy_cord[0] == const.PLAYER_SQUARES_SEQUENCE[-1][0] and piece.xy_cord[1] == const.PLAYER_SQUARES_SEQUENCE[-1][1]:
            result = piece
    return result

def addPieceToBoard(player):
    if len(player.pieces)  < const.TOTAL_NUM_OF_PLAYER_PIECES - player.score and not player.getPieceAtLocation(const.PLAYER_SQUARES_SEQUENCE[0]):
            player.addPieceToBoard()

def scorePoint(player, piece):
    player.score += 1
    player.pieces.remove(piece)


# checks if key has been press
# only returns true when the key has been press after not being pressed 
# ie. returns false if key is being held
def __hasKeyBeenPressed(pressed_keys, last_pressed_keys, key):
    return pressed_keys[key] and last_pressed_keys[key] != pressed_keys[key]    


if __name__ == "__main__":
    main()