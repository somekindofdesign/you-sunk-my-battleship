"""
This is a battleship style game made using Python 3.0.
"""

# Import random module
import random

# Import pyfiglet module
import pyfiglet


# Source: https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/
battle_cry = pyfiglet.figlet_format("Let's battle!", font="alligator2")
print("")
print(battle_cry)


class BattleshipBoard:
    """
    Class to build grid and generate boards.
    """

    letters_by_numbers = {"A": 0, "B": 1, "C": 2,
                          "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}

    def __init__(self, board):
        """
        Initialises the class.
        """
        self.board = board

    def generate_board(self):
        """
        Defines function to layout the battleship board.
        """
        print("/n     a   b   c   d   e  ")
        xaxis_number = 1
        for xaxis in self.board:

            # Uses % formatting placeholders to create the grid layout
            # Source: https://www.youtube.com/watch?v=alJH_c9t4zw
            print(" %d ¦ %s ¦ " % (xaxis_number, " ¦ ".join(xaxis)))
            xaxis_number += 1


class Battleships:
    """
    Class to generate ships and handle players moves.
    """

    def __init__(self, board):
        self.board = board

    def generate_ships(self):
        """
        Defines function to position ships randomly on the board.
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
        Defines function to get and validate player moves on x and y axes.
        """
        print("\n")
        try:
            x_xaxis = input("What number do you want to try?: \n")
            while x_xaxis not in '12345':
                print("That's not a number from 1 to 5.")
                x_xaxis = input("Try again: /n")

            y_yaxis = input("\nWhat letter do you want to try?: \n").upper()
            while y_yaxis not in "ABCDE":
                print("That's not a letter from A to E.")
                y_yaxis = input("Try again: ").upper()
            return (
                int(x_xaxis) - 1, BattleshipBoard.letters_by_numbers[y_yaxis])
        except ValueError:
            print("Sorry, I don't recognise that entry - please try again.")
        return self.player_move()

    def sunk_ships_score(self):
        """
        Define function to keep track of score after player inputs move.
        """
        sunk_ships = 0
        for xaxis in self.board:
            for yaxis in xaxis:
                if yaxis == "X":
                    sunk_ships += 1
        return sunk_ships


def play_battleships():
    """
    Defines function for game play.
    """
    game_board = BattleshipBoard([[" "] * 5 for i in range(5)])
    moves_board = BattleshipBoard([[" "] * 5 for i in range(5)])
    Battleships.generate_ships(game_board)

    # set number of torpedoes to play with
    torpedoes = 8
    while torpedoes > 0:
        BattleshipBoard.generate_board(moves_board)

        # get next player move
        player_x_xaxis, player_y_yaxis = Battleships.player_move(object)
        print(" \n")

        # checks for repeat moves
        while (moves_board.board[player_x_xaxis][player_y_yaxis] == "X" or
                moves_board.board[player_x_xaxis][player_y_yaxis] == "-"):
            print("A torpedo already landed here - try another move.")
            player_x_xaxis, player_y_yaxis = Battleships.player_move(object)

        # checks if torpedo hit a ship
        if game_board.board[player_x_xaxis][player_y_yaxis] == "X":
            print("You sunk my battleship!\n")
            moves_board.board[player_x_xaxis][player_y_yaxis] = "X"
        else:
            print("You missed my battleships!\n")
            moves_board.board[player_x_xaxis][player_y_yaxis] = "-"

        # checks if all ships have been hit or torpedoes ran out
        if Battleships.sunk_ships_score(moves_board) == 5:
            print("You sunk all my battleships!\n")
            # Source:
            # https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/
            winners_cry = pyfiglet.figlet_format("You have won the battle but not the war!", font="banner3-D")
            print("")
            print(winners_cry)
            break
        else:
            torpedoes -= 1
            print(f"There are {torpedoes} torpedoes left in your arsenal.\n")

        if torpedoes == 0:
            print("You ran out of torpedoes and lost the battle.\n")
            play_again = str(input("Want another battle? Type yes or no: \n"))
            if play_again.lower() == "yes":
                play_battleships()
            elif play_again.lower() == "no":
                print("You've been dishonourably discharged. Goodbye!")
                quit()
            else:
                print("\nType yes or no, please!\n")
                

# Intro to the game, asks the user if they wish to play
while True:
    player_input = input(
        "Do you want to play a game of battleships with me? Type yes or no: ")

    if player_input.lower() == "yes":
        print("\nGreat! I'll set up the board...")
        # let's play Battleships!
        # Source: https://www.youtube.com/watch?v=alJH_c9t4zw
        if __name__ == '__main__':
            play_battleships()
    elif player_input.lower() == "no":
        print("Oh well. Maybe later!")
        break
    else:
        print("Type yes or no, please!\n")
