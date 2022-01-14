import requests
api_url = 'https://api.coinlore.net/api/tickers/?start=0&limit=50'

res = requests.get(api_url).json()
data = res['data']

print("THIS PROGRAM IS TO FIND THE CRYPTO'S PRICE BRIEFLY")

for info in data:
    print("")
    print(f"Name: {info['name']}")
    print(f"NameId: {info['nameid']}")
    print(f"Rank: {info['rank']}")
    print(f"Symbol: {info['symbol']}")
    print(f"Price: ${info['price_usd']} per {info['symbol']}")
    print("")