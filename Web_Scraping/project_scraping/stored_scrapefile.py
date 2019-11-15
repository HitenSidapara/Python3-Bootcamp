# csv file store data load in this file
# http://quotes.toscrape.com/

import requests
from bs4 import BeautifulSoup
from random import choice
from csv import DictReader

base_url = "http://quotes.toscrape.com"
url= "/page/1/"

def csv_file_read(filename):
    with open(filename,"r") as file:
        csv_read = DictReader(file)
        return list(csv_read)


def start_game(all_quotes):
    choice_quote = choice(all_quotes)
    remaining_number =4
    print(choice_quote["text"])
    print(choice_quote["author"])
    guess = " "

    while guess.lower() != choice_quote["author"].lower() and remaining_number>0:
        guess = input(f"Who said this quote? Guesses Remaining {remaining_number} : ")

        if guess.lower() == choice_quote["author"].lower():
            print("You Are Win the Game")
            break

        remaining_number-=1
        if remaining_number == 3:
            res = requests.get(f"{base_url}{choice_quote['bio-link']}")
            soup = BeautifulSoup(res.text,"html.parser")
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_place = soup.find(class_="author-born-location").get_text()
            print(f"Hear's a hint : the author was born on {birth_date} {birth_place}")
        elif remaining_number == 2:
            print(f"Hear's a hint : The author first name letter start with : {choice_quote['author'][0]}")

        elif remaining_number == 1:
            last_name = choice_quote["author"].split(" ")[1][0]
            print(f"Hear's a hint : The author last name letter start with : {last_name}")
        else:
            print(f"You are loss the game. The author was {choice_quote['author']}")


    again=""
    while again.lower() not in ('yes','y','no','n'):
        again = input("Would You like to play again (y/n)?")
    if again in ('yes','y'):
        return start_game(all_quotes)
    else:
        print("Good Bye!")


# Calling the function
all_quotes = csv_file_read("quotes.csv")
start_game(all_quotes)