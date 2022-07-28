import requests
url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=YTO6ABLT1Z3PLSFS"
response = requests.get(url)
data = response.json()
print(data)
