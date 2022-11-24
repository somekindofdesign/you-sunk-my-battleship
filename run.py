player_input = ''

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