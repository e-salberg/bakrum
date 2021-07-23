# bakrum

## general info
this project is just for some practice with make a project from skretch and work on implementing an idea and then reflecting on the execution. the game is based on an old board game called Ur.


To run:  ```python3 game.py```
## Game play

Two player game, player 1 controls white pieces and player 2 controls black pieces. Players take turns rolling a random number between 0 - 4 and moving a piece that many squares. Player 1's starting square is the green left arrow in the top row while Player 2's starting square is the green left arrow in the bottom row. Pieces move left until end of the board and then up into the middle row and move right until reaching the right edge of board. Once at the right edge, Player 1 pieces will move up while Player 2 pieces move down. Each player has 7 pieces and the game end when one player has moved all pieces through the board and reach the end of their path.

### Note:
- Only Player 1's pieces can be in the top row while only Player 2's pieces can be in the bot row
- Pieces consume one point of movement to move onto/off the board
- A Player can only move one piece per turn and that piece must move the full roll
- Only one piece can occupy a square at a time
- A player cannot move a piece if one of their pieces if already occuping the destination square
- If player 1 moves a piece onto a square that is holding a player 2 piece then player 2 piece is removed from the board and vise versa

## Controls:

- W, A, S, D - move up, left, down, right
- enter/return - move piece
- 0 - add piece to board
