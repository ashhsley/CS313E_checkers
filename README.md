# CS313E_checkers
a simple checkers game

class Piece # checkers piece

INIT
- color (1 or 2)
- isKing (t/f)
- (?) position [x, y]

class Board #8x8 board

INIT
- board [][] <fill out at beginning
- put all pieces at starting pos
- turn (0 = black or 1 = white) initially 0
- black_pieces []
- white_pieces []

turn()
-check poss turns
-check whos turn
-action
- check for king
-check if won

validMoves(0 = black or 1 = white) #what moves are possible 
return Set of poss position

checkWin()
-ran out of pieces
-ran out of moves

printBoard()

MAIN
- init board
- prompt for input from player black/white
- loop til win
