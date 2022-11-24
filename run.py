player_input = ''
"""
Intro to the game, asks the user if they wish to play
"""
while True:
    player_input = input("Do you want to play a game of battleships with me? Type yes or no: ")

    if player_input.lower() == "yes":
        print("Great! I'll set up the boards...")
        break
    elif player_input.lower() == "no":
        print("Oh well. Mayber later!")
        break
    else:
        print("Type yes or no, please!")

"""
Generates the boards
"""
player_board=[[' ']*8 for x in range(8)]
board_grid={'A':0,'B':1, 'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}
print(player_board)