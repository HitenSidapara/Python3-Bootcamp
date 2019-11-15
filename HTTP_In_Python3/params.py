import requests

url = "https://icanhazdadjoke.com/search"

res = requests.get(
    url,
    headers = {"Accept":"Application/json"},
    params={"term": "cat", "limit": 1}
)
data = res.json()

# print(data);

print(data["results"]);

