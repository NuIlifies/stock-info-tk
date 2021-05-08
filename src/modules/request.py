# This file exists to handle requests between the application and RapidAPI. Returns result as JSON.
# API key is held in my own file covered by gitignore. Replace it with whatever you want.   
# JSON parsing must be performed elsewhere.
from modules import key as k
import requests

url = "https://yahoo-finance-low-latency.p.rapidapi.com/v6/finance/"

headers = {
    'x-rapidapi-key': k.key,
    'x-rapidapi-host': "yahoo-finance-low-latency.p.rapidapi.com"
}

# Valid Operations: chart, history, options, quotes, quoteSummary
def makeRequest(symbols, operation):
    # Since each operation has a differnet name i.e. tickers, symbols, etc. the key can be changed to fit its corresponding operation
    nameForSymbol = None
    
    if operation == "chart":
        nameForSymbol = "ticker"
        if len(symbols > 1):
            return None
    elif operation == "quote":
        nameForSymbol = "symbols"
    
        
    query = {nameForSymbol:symbols, "region":"US"}
    response = requests.request("GET", url + operation, headers=headers, params=query)
    return response.json()