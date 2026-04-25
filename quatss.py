import requests

url = "https://api.quotable.io/quotes/random"
response = requests.get(url)
data = response.json()

print("Quote:", data["content"])
print("Author:", data["author"])