def api_function():
    """
    - This function has no given parameter.
    - This function will convert the computed amounts from the other tasks from USD to SGD.
    - This function uses real-time exchange rates from the API call by accessing the nested dictionary from url.
    """
    from pathlib import Path
    import requests

    ##to extend the file path to the final text file, where all the computed amounts will be contained in.
    summary = Path.cwd()/"summary_report.txt"

    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey="YTO6ABLT1Z3PLSFS"'
    #to read an existing resource.
    response = requests.get(url)
    data = response.json()

    #to extract the exchange rate from the nested dictionary.
    currency_exchange_rate = data['Realtime Currency Exchange Rate']['5. Exchange Rate']
    #to convert it to a float and assign it to a variable of "CURRENCY_EXCHANGE_RATE".
    CURRENCY_EXCHANGE_RATE = float(currency_exchange_rate)

    #create "writer" object and include newline to prevent an extra line from being added to the end of the CSV file.
    with summary.open(mode = "w", encoding = "UTF-8", newline = "") as file:
        #to assign the final output that will be displayed in the summary_report to the variable of 'Output' on a new line.
        Output = (f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{CURRENCY_EXCHANGE_RATE}")
        #to write the output to summary_report.
        file.write(Output)
        #to close the file (summary).
        file.close()
    return CURRENCY_EXCHANGE_RATE