# Rock beats Scissors
# scissors beats paper
# paper beats Rock



from random import randint;

print(".....Rock........");
print(".....Paper.......");
print(".....scissors....");


# input of the game


player = input("Player , make your move : ").lower();


rand_number = randint(0,2);

if rand_number == 0:
    computer = "rock";
elif rand_number == 1:
    computer = "paper";
else:
    computer = "scissors";

print(f"computer move is {computer}");

# logic of the game

if player==computer:
    print("Game is tie!");

elif player == "rock" :
    if computer == "scissors":
         print("Player  win!");
    else:
        print("computer win :(");

elif player == "paper":
    if computer == "rock":
        print("Player win!");
    else:
        print("computer win :(");

elif player == "scissors":
    if computer == "paper":
        print("Player win!");
    else:
        print("computer win :(");
else:
    print("Something went to wrong");