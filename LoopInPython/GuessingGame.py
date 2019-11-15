from random import randint;

computer_number = randint(1, 10);

# print(computer_number);

while True:

    guessing_number = int(input("Guess The Number Between 1 to 10 : "));

    if guessing_number > computer_number:
        print("Too High, Try Again!");
    elif guessing_number < computer_number:
        print("Too Low, Try Again!");
    else:
        print("You Guessed it! You Won!");

        play_again = input("Do You Want YO play Again?(y/n) ");

        if play_again == "y":
            computer_number = randint(1, 10);
            guessing_number = None;
        else:
            print("Thanks For Playing Game, Bye!");
            break;
