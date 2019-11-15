import requests
from random import choice
from pyfiglet import figlet_format
from termcolor import  colored


# header section

header = figlet_format("DAD  JOKE ! !")
header_color = colored(header,color="magenta")
print(header_color)

# user input

user_input = input("What would you like to search for ? ")

# logical part

url = "https://icanhazdadjoke.com/search"

res = requests.get(
    url,
    headers = {"Accept":"Application/json"},
    params={"term": user_input}
).json()


num_joke = len(res['results'])

# check the condtions

if num_joke > 1:
    print(f"I found {num_joke} about {user_input} Hears One")
    print(choice(res['results'])["joke"])
elif num_joke == 1:
    print(f"I found One Joke Anout {user_input}")
    print(res['results'][0]['joke'])
else:
    print(f"Sorry we can not find your joke term : {user_input}")