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

    p1 = Player(const.P1_MAPPINGS)
    p2 = Player(const.P2_MAPPINGS)
    brd = Board()

    font = pygame.font.Font('freesansbold.ttf', 50)

    # create a text suface object,
    # on which text is drawn on it.
    p1_score_text = font.render('0', True, const.P1_MAPPINGS['color'])
    p2_score_text = font.render('0', True, const.P2_MAPPINGS['color'])

    # create a rectangular object for the
    # text surface object
    p1TextRect = p1_score_text.get_rect()
    p1TextRect.center = const.P1_MAPPINGS['score_center']
    p2TextRect = p2_score_text.get_rect()
    p2TextRect.center = const.P2_MAPPINGS['score_center']

    # keep track of keys pressed last frame to prevent keys held down from triggering events
    last_pressed_keys = pygame.key.get_pressed()

    spaces_to_travel = randint(const.MIN_MOVE, const.MAX_MOVE)
    movement_text = font.render(str(spaces_to_travel), True, const.BLUE)
    movementTextRect = movement_text.get_rect()
    movementTextRect.center = (640, 365)

    # player one's turn, if false then player two's turn
    p1_turn = True

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

        if p1_turn:
            next_roll = updatePlayerTurn(p1, p2, last_pressed_keys, spaces_to_travel)
            if next_roll is not None:
                p1_turn = not p1_turn
                spaces_to_travel = next_roll
                movement_text = font.render(str(next_roll), True, const.BLUE)
        else:
            next_roll = updatePlayerTurn(p2, p1, last_pressed_keys, spaces_to_travel)
            if next_roll is not None:
                # check if piece moved to special square
                p1_turn = not p1_turn
                spaces_to_travel = next_roll
                movement_text = font.render(str(next_roll), True, const.BLUE)


        scoredPiece = pieceReachedGoal(p1)
        if scoredPiece is not None:  # and scoredPiece is not p1.selected_piece:
            scorePoint(p1, scoredPiece)
            p1_score_text = font.render(str(p1.score), True, const.P1_MAPPINGS['color'])
            if p1.score == const.TOTAL_NUM_OF_PLAYER_PIECES:
                done = True

        scoredPiece = pieceReachedGoal(p2)
        if scoredPiece is not None:  # and scoredPiece is not p1.selected_piece:
            scorePoint(p2, scoredPiece)
            p2_score_text = font.render(str(p2.score), True, const.P2_MAPPINGS['color'])
            #if score = total num of player pieces -> end game
            if p2.score == const.TOTAL_NUM_OF_PLAYER_PIECES:
                done = True
        

        # fill background with white
        screen.fill((0, 0, 0))

        # draw game board
        brd.draw(screen)

        # draw player
        p1.draw(screen, p1_turn)
        p2.draw(screen, not p1_turn)

        # draw text
        screen.blit(p1_score_text, p1TextRect)
        screen.blit(p2_score_text, p2TextRect)
        screen.blit(movement_text, movementTextRect)

        # updates the contents of the display to the screen. Without this call, nothing appears in the window
        pygame.display.flip()

        # keep track of keys pressed last frame to prevent keys held down from triggering events
        last_pressed_keys = pygame.key.get_pressed()

    pygame.quit()


def updatePlayerTurn(player, other_player, last_pressed_keys, spaces_to_travel):
    # Get all the current pressed keys and process results
        next_roll = None
        pressed_keys = pygame.key.get_pressed()
        if __hasKeyBeenPressed(pressed_keys, last_pressed_keys, K_0):
            if addPieceToBoard(player, spaces_to_travel):
                # roll dice for new amount to move if piece was added to board
                next_roll = randint(const.MIN_MOVE, const.MAX_MOVE)
                
        elif __hasKeyBeenPressed(pressed_keys, last_pressed_keys, K_RETURN):
            piece = player.getPieceAtLocation(const.BOARD_SQUARES_LOCATIONS[player.row][player.col])
            if spaces_to_travel == 0 or not player.hasAtLeastOneValidMove(spaces_to_travel):
                # if roll 0 or player can't move any pieces just end turn if enter key is pressed
                # roll dice for new amount to move
                next_roll = randint(const.MIN_MOVE, const.MAX_MOVE)
            elif player.canPlayerMovePiece(piece, spaces_to_travel):
                player.movePiece(piece, spaces_to_travel)
                # check if piece moved into other player's pieces
                other_players_piece = other_player.getPieceAtLocation(piece.xy_cord)
                if other_players_piece is not None:
                    other_player.pieces.remove(other_players_piece)
                # roll dice for new amount to move
                next_roll = randint(const.MIN_MOVE, const.MAX_MOVE)

        player.update(pressed_keys, last_pressed_keys)
        return next_roll



def pieceReachedGoal(player):
    result = None
    for piece in player.pieces:
        # piece_location = const.BOARD_SQUARES_LOCATIONS[piece.row][piece.col]
        if piece.xy_cord[0] == player.move_seq[-1][0] and piece.xy_cord[1] == player.move_seq[-1][1]:
            result = piece
    return result

# a piece consumes 1 movement to move onto the board
# return true if a piece was added to board, false otherwise
def addPieceToBoard(player, spaces_to_travel):
    if len(player.pieces) < const.TOTAL_NUM_OF_PLAYER_PIECES - player.score and spaces_to_travel > 0 and not player.getPieceAtLocation(player.move_seq[spaces_to_travel - 1]):
        player.addPieceToBoard(spaces_to_travel - 1)
        return True
    return False


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
