# Scrape Data and store into the file(csv)

# http://quotes.toscrape.com/

import requests
from bs4 import BeautifulSoup
from  time import sleep
from random import choice
from csv import DictWriter

base_url = "http://quotes.toscrape.com"
url= "/page/1/"



def scrape_quote():

    all_quotes = []
    global url
    while url:
        res = requests.get(f"{base_url}{url}")
        print(f"Scrapping {base_url}{url}")
        soup = BeautifulSoup(res.text,"html.parser")
        quotes = soup.find_all(class_="quote")

        for quote in quotes:
            all_quotes.append({
                "text":quote.find(class_="text").get_text(),
                "author":quote.find(class_="author").get_text(),
                "bio-link":quote.find("a")["href"]
            })

        next_btn = soup.find(class_="next")
        url = next_btn.find("a")["href"] if next_btn else None
        sleep(1)
    return all_quotes



# Save the data to the csv file
def write_quotes(quotes):
    with open("quotes.csv","w") as file:
        header = ["text","author","bio-link"]
        csv_writer = DictWriter(file,fieldnames=header)
        csv_writer.writeheader()
        for quote in quotes:
            csv_writer.writerow(quote)



# calling the function

quotes = scrape_quote()
write_quotes(quotes)