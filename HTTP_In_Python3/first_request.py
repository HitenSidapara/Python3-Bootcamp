import requests

url = "https://www.google.com/"
res = requests.get(url)

print(f"{url} responce status code is {res.status_code} ")

print(res.headers)
print(res.text)