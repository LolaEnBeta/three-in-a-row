from Player import Player
from Board import Board

BOARD_SIZE = 3

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

new_board = Board(3)
board = new_board.create_board()
new_board.print_board()

try:
    turns = 4
    while turns > 0:
        player_1.player_turn(board)
        new_board.print_board()
        print("")
        player_2.player_turn(board)
        new_board.print_board()
        print("")
        turns -= 1
finally:
    print("Boards! No one win =(")
