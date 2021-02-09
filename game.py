import pygame
import constants as const
from player import Player
from board import Board
from random import randint

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
    score_text = font.render('0', True, const.BLUE)

    # create a rectangular object for the
    # text surface object
    textRect = score_text.get_rect()
    textRect.center = const.PLAYER_SCORE_CENTER

    # keep track of keys pressed last frame to prevent keys held down from triggering events
    last_pressed_keys = pygame.key.get_pressed()

    spaces_to_travel = randint(1, 4)
    movement_text = pygame.font.Font('freesansbold.ttf', 50)
    movement_text = font.render(str(spaces_to_travel), True, const.BLUE)
    movementTextRect = movement_text.get_rect()
    movementTextRect.center = (640, 365)

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
            addPieceToBoard(p1, spaces_to_travel)
            # roll dice for new amount to move
            spaces_to_travel = randint(1, 4)
            movement_text = font.render(str(spaces_to_travel), True, const.BLUE)
        elif __hasKeyBeenPressed(pressed_keys, last_pressed_keys, K_RETURN):
            piece = p1.getPieceAtLocation(const.BOARD_SQUARES_LOCATIONS[p1.row][p1.col])
            if spaces_to_travel != 0 and p1.canPlayerMovePiece(piece, spaces_to_travel):
                p1.movePiece(piece, spaces_to_travel)
                # roll dice for new amount to move
                spaces_to_travel = randint(1, 4)
                movement_text = font.render(str(spaces_to_travel), True, const.BLUE)

        p1.update(pressed_keys, last_pressed_keys)

        scoredPiece = pieceReachedGoal(p1)
        if scoredPiece is not None:  # and scoredPiece is not p1.selected_piece:
            scorePoint(p1, scoredPiece)
            score_text = font.render(str(p1.score), True, const.BLUE)

        # fill background with white
        screen.fill((0, 0, 0))

        # draw game board
        brd.draw(screen)

        # draw player
        p1.draw(screen)

        # draw text
        screen.blit(score_text, textRect)
        screen.blit(movement_text, movementTextRect)

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

# a piece consumes 1 movement to move onto the board


def addPieceToBoard(player, spaces_to_travel):
    if len(player.pieces) < const.TOTAL_NUM_OF_PLAYER_PIECES - player.score and not player.getPieceAtLocation(const.PLAYER_SQUARES_SEQUENCE[spaces_to_travel - 1]):
        player.addPieceToBoard(spaces_to_travel - 1)


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
