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
        letters_by_numbers = {"A": 0, "B": 1, "C": 2,
                              "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
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


class Battleships:
    """
    Class to generate ships and handle players moves
    """

    def __init__(self, board):
        self.board = board

    def generate_ships(self):
        """
        Defines function to position ships randomly on the board
        """
        for i in range(4):
            self.x_xaxis, self.y_yaxis = random.randint(
                0, 4), random.randint(0, 4)
            while self.board[self.x_xaxis][self.y_yaxis] == "X":
                self.x_xaxis, self.y_yaxis = random.randint(
                    0, 4), random.randint(0, 4)
            self.board[self.x_xaxis][self.y_yaxis] = "X"
        return self.board

    def player_move(self):
        """
        Defines function to get and validate player moves on x and y axes
        """
        try:
            x_xaxis = input("What number do you want to try?: ")
            while x_xaxis not in '12345':
                print("That's not a number from 1 to 5.")
                x_xaxis = input("Try again: ")

            y_yaxis = input("What letter do you want to try?: ").upper()
            while y_yaxis not in "ABCDE":
                print("That's not a letter from A to E.")
                y_yaxis = input("Try again: ").upper()
            return int(x_xaxis) - 1, BattleshipBoard.board_letters_by_numbers()[y_yaxis]
        except ValueError:
            print("Sorry, I don't recognise what you entered - please try again.")
        return self.player_move()

    def sunk_ships_score(self):
        """
        Define function to keep track of score after player inputs move
        """
        sunk_ships = 0
        for xaxis in self.board:
            for yaxis in xaxis:
                if yaxis == "X":
                    sunk_ships += 1
        return sunk_ships


def PlayBattleships():
    """
    Defines function for game play
    """
    game_board = BattleshipBoard([[" "] * 5 for i in range(5)])
    moves_board = BattleshipBoard([[" "] * 5 for i in range(5)])
    Battleships.generate_ships(game_board)