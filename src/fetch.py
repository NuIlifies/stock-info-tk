import requests
url = "https://yahoo-finance-low-latency.p.rapidapi.com/v6/finance/quote"

headers = {
    'x-rapidapi-key': "d81a20f172mshc140a4f4e3971fep1704cbjsn4df8c8a8184e",
    'x-rapidapi-host': "yahoo-finance-low-latency.p.rapidapi.com"
}

def get(symbols):   
    query = {"symbols":symbols, "region":"US"}
    response = requests.request("GET", url, headers=headers, params=query)
    jsonResponse = response.json()


    # SYMBOLS ARE APPENDED TO LIST IN CASE NUMEROUS SYMBOLS ARE PASSED
    symbolsList = []
    print(len(jsonResponse['quoteResponse']['result']))


    if len(jsonResponse['quoteResponse']['result']) == 0:
        return "Invalid symbol '{}'".format(symbols[0])
    else:
        for x in range(len(jsonResponse['quoteResponse']['result'])):
            symbolsList.append(jsonResponse['quoteResponse']['result'][x]['longName'])
    return symbolsList
