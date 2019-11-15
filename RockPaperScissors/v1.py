# Rock beats Scissors
# scissors beats paper
# paper beats Rock



print("Rock........");
print("Paper.......");
print("scissors....");


player1 = input("player 1, make your move : ");
player2 = input("player 2, make your move : ");


if player1 == "rock" and player2 == "scissors":
    print("player 1 win!");
elif player1 == "rock" and player2 =="paper":
    print("player 2 win!");
elif player1 == "paper" and player2 == "rock":
    print("player 1 win!");
elif player1 =="paper" and player2 == "scissors":
    print("player 2 win!");
elif player1 == "scissors" and player2 == "rock":
    print("player 2 win!");
elif player1 == "scissors" and player2 == "paper":
    print("player 1 win!");
elif player1==player2:
    print("Game is tie!");
else:
    print("Something went to wrong");