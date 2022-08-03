def api_function():
    """
    - This function has no given parameter.
    - This function will convert the computed amounts from the other tasks from USD to SGD.
    - This function uses real-time exchange rates from the API call by accessing the nested dictionary from url.
    """
    from pathlib import Path
    import requests

    summary = Path.cwd()/"project_group"/"summary_report.txt"

    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey="YTO6ABLT1Z3PLSFS"'
    response = requests.get(url)
    data = response.json()

    currency_exchange_rate = data['Realtime Currency Exchange Rate']['5. Exchange Rate']
    CURRENCY_EXCHANGE_RATE = float(currency_exchange_rate)

    with summary.open(mode = "w", encoding = "UTF-8", newline = "") as file:
        Output = (f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{CURRENCY_EXCHANGE_RATE}")
        file.write(Output)
        file.close()
    return CURRENCY_EXCHANGE_RATE
