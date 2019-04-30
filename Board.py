
class Board:
    def __init__(self, board_size):
        self.board_size = board_size
    
    def create_board(self):
        self.board = []
        self.board_size
        for i in range(self.board_size):
            row = []
            for j in range(self.board_size):
                j = "-"
                row.append(j)
            self.board.append(row)
        return self.board

    def print_board(self):
        for i in range(self.board_size):
            print(self.board[i])
