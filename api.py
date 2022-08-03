def api_function():
    """
    """
    from pathlib import Path
    import requests

    summary = Path.cwd()/"project_group"/"summary_report.txt"

    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey="YTO6ABLT1Z3PLSFS"'
    
