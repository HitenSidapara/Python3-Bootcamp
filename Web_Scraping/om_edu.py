# http://omeducation.edu.in/om_com.php

import requests
import csv
from bs4 import BeautifulSoup

responce = requests.get("http://omeducation.edu.in/om_com.php");

data= responce.text

# print(data)

soup = BeautifulSoup(data,"html.parser")


# title = soup.find_all(attrs={"style":"color:#2aa4a5;font-size:20px;"})
#
# for i in range(0,5):
#     print(title[i].text)


table = soup.find(class_="table table-striped table-colored")

# print(table)

heading = soup.findAll("th")

tbody = soup.find("tbody")

tr = tbody.findAll("tr")

computer_list = []

with open("om.csv","w") as file:
    csv_write = csv.writer(file)
    csv_write.writerow(heading)
    for tr_data in range(0, len(tr)):
        data = tr[tr_data].text
