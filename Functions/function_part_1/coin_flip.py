from random import randint;

def flip_coin():
    # create the random number

    # number = randint(0,1)

    # if the number is the 1 return heads
    # else return the tails
    if randint(0,1) == 1:
        return "Heads"
    else:
        return "Tails"

print(f"Result is : {flip_coin()}");