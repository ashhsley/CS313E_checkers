class Piece:
    def __init__(self, color = 1, position = [0,0]):
        self.color = color
        self.isKing = False
        self.position = position

class Board:
    def __init__(self):
        self.black_pieces = []
        self.white_pieces = []
        #initialize board as an 8x8 array full of 0's. 
        self.board = []
        for i in range(8): 
            self.board.append([])
            for j in range(8):
                self.board[i].append(0)

    def turn():
        pass

    def validMoves():
        pass

    def checkWin():
        pass

    def printBoard():
        pass

###################################
#           MAIN METHOD           #
###################################

def main():
    playBtn = input('Welcome to Checkers! Press ENTER to play!') #starting screen
    if playBtn == '': 
        board = Board() #initializes game.

        #print rules?
        rulesPage = input('RULES:\nThis is a two player game.\nPress ENTER to start.')
        if rulesPage =='':
            print(board.printBoard())
            ###############
            #  Turn loop  #
            ###############
            while not board.checkWin():
                #one turn
                pass
            print('winner wins!') 


if __name__ == "__main__":
    main()