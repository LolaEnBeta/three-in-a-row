from Player import Player

BOARD_SIZE = 3

def create_a_board():
    table_board = []
    for i in range(BOARD_SIZE):
        row = []
        for j in range(BOARD_SIZE):
            j = "-"
            row.append(j)
        table_board.append(row)
    return table_board

def print_board():
    print(table_board[0])
    print(table_board[1])
    print(table_board[2])

name_player_1 = input("Player 1, what is your name? ")
symbol_player_1 = input("And what symbol do you want? ")
print("")
name_player_2 = input("Player 2, what is your name? ")
symbol_player_2 = input("And what symbol do you want? ")

player_1 = Player(name_player_1, symbol_player_1)
player_2 = Player(name_player_2, symbol_player_2)

print("")
player_1.presentation()
player_2.presentation()
print("")

table_board = create_a_board()
print_board()

try:
    turns = 4
    while turns > 0:
        player_1.player_turn(table_board)
        print_board()
        print("")
        player_2.player_turn(table_board)
        print_board()
        print("")
        turns -= 1
finally:
    print("Boards! No one win =(")
