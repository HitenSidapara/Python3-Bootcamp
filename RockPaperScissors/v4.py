# autopep8 --in-place [File name of python]   ===== used for the indention

# Rock beats Scissors
# scissors beats paper
# paper beats Rock


from random import randint

print(".....Rock........");
print(".....Paper.......");
print(".....scissors....");

# input of the game

player_wins = 0
computer_wins = 0
winning_score = 4

while player_wins < winning_score and computer_wins < winning_score:

    print(f"Player Score : {player_wins}  ==== Compure Score : {computer_wins}")

    player = input("Player, make your move : ").lower()

    if player == "quite" or player == "q":
        break

    rand_number = randint(0, 2)

    if rand_number == 0:
        computer = "rock"
    elif rand_number == 1:
        computer = "paper"
    else:
        computer = "scissors"

    print(f"computer move is {computer}")

    # logic of the game

    if player == computer:
        print("Game is tie!")

    elif player == "rock":
        if computer == "scissors":
            player_wins += 1
            print("Player  win!")
        else:
            computer_wins += 1
            print("computer win :(")

    elif player == "paper":
        if computer == "rock":
            player_wins += 1
            print("Player win!")
        else:
            computer_wins += 1
            print("computer win :(")

    elif player == "scissors":
        if computer == "paper":
            player_wins += 1
            print("Player win!")
        else:
            computer_wins += 1
            print("computer win :(")
    else:
        print("Something went to wrong")

if player_wins > computer_wins:
    print("Congrats You Are Win :)")
elif player_wins == computer_wins:
    print("Oh No Game Is Tie")
else:
    print("Soory, Computer Wins :(")


# print(f"Player Score : {player_wins}  ==== Compure Score : {computer_wins}")
