<<<<<<< HEAD
=======
import requests
url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=YTO6ABLT1Z3PLSFS"
response = requests.get(url)
data = response.json()
print(data)
>>>>>>> 6ce5e7e70802f81b510cf4a65b9b8dc7f357850f
