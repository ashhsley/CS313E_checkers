# CS313E_Rack-O!!!
A simple card game with two players
The goal is to be the first to have a rack with cards that respect heap invariant (https://en.wikipedia.org/wiki/Binary_heap)
Players both start with racks of equal lengths populated with cards ranging from 1 to 60 dealt from a randomly shuffled deck

class Rack

INIT
-rack[] containing the cards currently in hands

class TreeRack

INIT
-rack

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
