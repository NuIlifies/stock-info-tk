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
    elif searchParam.upper() == "RAW_RESPONSE":
        return raw_response(symbols)
    elif searchParam.upper() == "PRICE":
        return price(symbols)
    else:
        return "Invalid operation '{}'".format(searchParam)


#make request and return request json
def makeRequest(symbols):
    query = {"symbols":symbols, "region":"US"}
    response = requests.request("GET", url, headers=headers, params=query)
    return response.json()

# Actually parse the returned json data sing given parameters.
def parseRequest(operation, jsonResponse):
    symbolsList = []

    if len(jsonResponse['quoteResponse']['result']) == 0:
        return "Invalid symbol '{}'".format(symbols)
    else:
    # If there actually is a result, then added the longName property to list
        try:
            for x in range(len(jsonResponse['quoteResponse']['result'])):
                symbolsList.append(jsonResponse['quoteResponse']['result'][x][operation])
        except IndexError:
            symbolsList = "Error retrieving information from symbol(s) {}".format(symbols)
        except KeyError:
            symbolsList = "Error retrieving information from symbol(s) {}".format(symbols)

    #If there is only one result, then just return it as a string and not a list. Lists are reserved for numerous queries.
    if len(symbolsList) == 1:
        symbolsList = symbolsList[0]

    return symbolsList


def name(symbols):   
    jsonResponse = makeRequest(symbols)
    return parseRequest('longName', jsonResponse)

def price(symbols):
    jsonResponse = makeRequest(symbols)
    return parseRequest('bid', jsonResponse)

def raw_response(symbols):
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
                symbolsList.append(jsonResponse['quoteResponse']['result'][x])
        except IndexError:
            symbolsList = "Error retrieving information from symbol(s) {}".format(symbols)
        except KeyError:
            symbolsList = "Error retrieving information from symbol(s) {}".format(symbols)

    if len(symbolsList) == 1:
        symbolsList = symbolsList[0]

    return symbolsList
