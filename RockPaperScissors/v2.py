# Rock beats Scissors
# scissors beats paper
# paper beats Rock



print("Rock........");
print("Paper.......");
print("scissors....");


player1 = input("player 1, make your move : ");
print("No Cheating \n\n"*20);
player2 = input("player 2, make your move : ");

if player1==player2:
    print("Game is tie!");

elif player1 == "rock" :
    if player2 == "scissors":
         print("player 1 win!");
    elif player2 =="paper":
        print("player 2 win!");

elif player1 == "paper":
    if player2 == "rock":
        print("player 1 win!");
    elif player2 == "scissors":
        print("player 2 win!");

elif player1 == "scissors":
    if player2 == "rock":
        print("player 2 win!");
    elif player2 == "paper":
        print("player 1 win!");
else:
    print("Something went to wrong");