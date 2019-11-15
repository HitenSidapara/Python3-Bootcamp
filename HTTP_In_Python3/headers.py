import requests

url = "https://icanhazdadjoke.com/"

# res = requests.get(url);

# res = requests.get(url,headers = {"Accept":"text/plain"})

# res = requests.get(url,headers = {"Accept":"text/html"})

res = requests.get(url,headers = {"Accept":"Application/json"})

# print(res.text) type is string

# return the dictionary and now we are use it

# print(res.json())

data = res.json()

print(data['joke']);
print(f"Status {data['status']}")
