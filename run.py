import random

"""
player_input = ''

#Intro to the game, asks the user if they wish to play

while True:
    player_input = input(
        "Do you want to play a game of battleships with me? Type yes or no: ")

    if player_input.lower() == "yes":
        print("Great! I'll set up the boards...")
        break
    elif player_input.lower() == "no":
        print("Oh well. Mayber later!")
        break
    else:
        print("Type yes or no, please!")
"""

class BattleshipBoard:
    """
    Class to build grid and generate boards
    """
    def __init__(self, board):
        self.board = board

    def board_letters_by_numbers():
        """
        Defines function to reference letter and number grid
        """
        letters_by_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
        return letters_by_numbers

    def generate_board(self):
        """
        Defines function to layout the battleship board
        """
        print("  a b c d e")
        xaxis_number = 1
        for xaxis in self.board:

            # uses % formatting placeholders to create the grid layout
            print("%d¦%s¦" % (xaxis_number, "¦".join(xaxis)))
            xaxis_number += 1

print(BattleshipBoard)