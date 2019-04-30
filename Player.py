
class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def presentation(self):
        print("Hi, my name is", self.name, "and my symbol is", self.symbol)

    def player_turn(self, board):
        print(self.name, "'s turn")
        file = input("Choose one row (1, 2 or 3):")
        choose_file = int(file) - 1
        box = input("Choose one col (1, 2 or 3):")
        choose_box = int(box) - 1
        board[choose_file][choose_box] = self.symbol
