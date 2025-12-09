import requests

query = input("What type of news are you intrested in today? ")
api = "2f9b320e3e0240308c0d8d501a62f69e"


url = f"https://newsapi.org/v2/everything?q={query}&from=2025-10-19&sortBy=publishedAt&apiKey={api}"

print(url)
r = requests.get(url)

data = r.json()
articles = data["articles"]

for index, article in enumerate(articles):
    print(index + 1, article["title"], article["url"])
    print("\n********************************\n")