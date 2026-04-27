import requests
import time
key = "pub_1ee803101df54d119f0e3db176353036"
query = input("Enter the query: ")
url = f"https://newsdata.io/api/1/latest?apikey={key}&q={query}&language=en&category=technology,breaking"
start = time.time()
def news():
    response = requests.get(url)
    data = response.json()
    return data
news_data = news()
for news in news_data['results']:
    print(f"Title: {news['title']}")
    print("\n")
    print(f"Description: {news['description']}")
    print("\n")
print(f"its take {time.time() - start}sec")