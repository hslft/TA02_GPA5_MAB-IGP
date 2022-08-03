def api_function():
    """
    """
    from pathlib import Path
    import requests

    summary = Path.cwd()/"project_group"/"summary_report.txt"

    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey="YTO6ABLT1Z3PLSFS"'
    response = requests.get(url)
    data = response.json()

    exchange_rate = data['Realtime Currency Exchange Rate']['5. Exchange Rate']
    EXCHANGE_RATE = float(exchange_rate)

    with summary.open(mode = "w", encoding = "UTF-8", newline = "") as file:
        Output = (f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{EXCHANGE_RATE}")
        file.write(Output)
        file.close()
    return EXCHANGE_RATE
