import requests
from pathlib import Path
def api_function():
    fp_summary = Path.cwd()/"project_group"/"summary_report.txt"
    url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=YTO6ABLT1Z3PLSFS"
    response = requests.get(url)
    data = response.json()
    currency_exchange_rate = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
    with fp_summary.open(mode="w",encoding="UTF-8-sig",newline="") as file:
        message = f"[REAL TIME CURRENCY EXCHANGE RATE] USD 1 = SGD{currency_exchange_rate}"
        file.write(message)
        file.close()
        return currency_exchange_rate



        