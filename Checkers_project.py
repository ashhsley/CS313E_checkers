class Piece:
    def __init__(self, color=None, is_king=False, is_in=True, position=(0, 0)):
        self.color = color
        self.isKing = is_king
        self.position = position
        self.in_game = is_in

    def __str__(self):
        display = 0
        if self.color == 'white':
            display = 1
        elif self.color == 'balck':
            display = 2

        return str(display)


class Board:
    def __init__(self):
        blank_piece = Piece()
        self.grid = [[blank_piece for col in range(8)] for row in range(8)]
        self.white = []
        self.black = []

        for row in range(3):
            for col in range(4):
                white_piece = Piece('white', False, True, (row, 2*col))
                black_piece = Piece('black', False, True, (7 - row, 7 - 2*col))
                self.grid[row][2*col] = white_piece
                self.grid[7 - row][7 - 2*col] = black_piece
                self.white.append(white_piece)
                self.black.append(black_piece)

    def display_board(self):
        # Display the current world. world is a rectangular matrix of
        # booleans. * for occupied, - for open cells, unoccupied
        print()
        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                if self.grid[r][c]:
                    print(self.grid[r][c], end=' ')
            print()


def main():
    game_board = Board()
    game_board.display_board()


main()

