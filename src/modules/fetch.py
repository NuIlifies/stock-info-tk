from time import ctime
from modules import request 

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

# Actually parse the returned json data sing given parameters.
# rawResponseBool is there to compensate for the raw_response operation which does not require much parsing.
def parseRequest(operation, jsonResponse, rawResponseBool):
    symbolsList = []

    if len(jsonResponse['quoteResponse']['result']) == 0:
        return "Invalid symbol '{}'".format(symbols)
    else:
    # If there actually is a result, then added the longName property to list
        try:
            for x in range(len(jsonResponse['quoteResponse']['result'])):
                if rawResponseBool == 0:
                    symbolsList.append(jsonResponse['quoteResponse']['result'][x][operation])
                else:
                    symbolsList.append(jsonResponse['quoteResponse']['result'][x])
        except IndexError:
            symbolsList = "Error retrieving information from symbol(s) {}".format(symbols)
        except KeyError:
            symbolsList = "Error retrieving information from symbol(s) {}".format(symbols)

    #If there is only one result, then just return it as a string and not a list. Lists are reserved for numerous queries.
    if len(symbolsList) == 1:
        symbolsList = symbolsList[0]

    if rawResponseBool == 0:
        responseForReturn = "Information '{}' fetched at ".format(operation) + ctime() + ": {}".format(symbolsList)
    else:
        responseForReturn = symbolsList
        
    return responseForReturn


def name(symbols):   
    jsonResponse = request.makeRequest(symbols, "quote")
    return parseRequest('longName', jsonResponse, 0)

def price(symbols):
    jsonResponse = request.makeRequest(symbols, "quote")
    return parseRequest('bid', jsonResponse, 0)

def raw_response(symbols):
    jsonResponse = request.makeRequest(symbols, "quote")
    return parseRequest(None, jsonResponse, 1)

