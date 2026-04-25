import requests

url = "https://uselessfacts.jsph.pl/api/v2/facts/today"
response = requests.get(url)
dat  = response.json()
print(dat["text"])
