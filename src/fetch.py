import requests
url = "https://yahoo-finance-low-latency.p.rapidapi.com/v6/finance/quote"

headers = {
    'x-rapidapi-key': "d81a20f172mshc140a4f4e3971fep1704cbjsn4df8c8a8184e",
    'x-rapidapi-host': "yahoo-finance-low-latency.p.rapidapi.com"
}

#assign proper function based on provided search parameter (what you wanna look for, i.e. name)
def assignParam(searchParam, symbols):
    if searchParam.upper() == "NAME":
        return name(symbols)


#make request and return request json
def makeRequest(symbols):
    query = {"symbols":symbols, "region":"US"}
    response = requests.request("GET", url, headers=headers, params=query)
    return response.json()


def name(symbols):   
    jsonResponse = makeRequest(symbols)

    # SYMBOLS ARE APPENDED TO LIST IN CASE NUMEROUS SYMBOLS ARE PASSED
    symbolsList = []

    # If nothing is returned, probably because a symbol was entered incorrectly
    if len(jsonResponse['quoteResponse']['result']) == 0:
        return "Invalid symbol '{}'".format(symbols)
    else:
    # If there actually is a result, then added the longName property to list
        try:
            for x in range(len(jsonResponse['quoteResponse']['result'])):
                symbolsList.append(jsonResponse['quoteResponse']['result'][x]['longName'])
        except IndexError:
            symbolsList = "Error retrieving information from symbol(s) {}".format(symbols)
        except KeyError:
            symbolsList = "Error retrieving information from symbol(s) {}".format(symbols)
    
    return symbolsList
