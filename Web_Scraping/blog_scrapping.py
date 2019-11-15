# https://www.rithmschool.com/blog

import requests
from bs4 import BeautifulSoup
from csv import writer


responce = requests.get("https://www.rithmschool.com/blog")
data = responce.text

soup = BeautifulSoup(data,"html.parser")
articles = soup.find_all("article")

with open("blog_data.csv","w") as file:
    csv_write = writer(file)
    csv_write.writerow(["title","link","date"])
    for article in articles:
        title = article.find("a").get_text()
        link = article.find("a")["href"]
        datetime = article.find("time")["datetime"]
        csv_write.writerow([title,link,datetime])
        # print(title,link,datetime)