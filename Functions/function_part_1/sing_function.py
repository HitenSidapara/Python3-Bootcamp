# def means the define the funaction

# Varsion 1 :

def sing_happy_birthday():
    print("Happy Birthday To You");
    print("Happy Birthday To You");
    print("Happy Birthday Dear You");
    print("Happy Birthday To You");

sing_happy_birthday();



# Version 2 :

def sing_happy_birthday(name):
    print("Happy Birthday To You");
    print("Happy Birthday To You");
    print(f"Happy Birthday Dear {name}");
    print("Happy Birthday To You");

sing_happy_birthday("Hiten");
sing_happy_birthday("Raj");
