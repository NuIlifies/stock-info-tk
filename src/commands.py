from modules import fetch as f
from modules import chart as c

# The class where your commands are going to be stored as methods
def notEnoughArgs(expectedNum):
    return "Insufficient number of arguments passed (expected {})".format(str(expectedNum))

class commands:
    def __init__(self):
        pass

    def fetch(searchParam, symbols):
        stockJson = f.assignParam(searchParam, symbols)
        return str(stockJson)

    def chart(symbol):
        pass

