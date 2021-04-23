import fetch as f

# The class where your commands are going to be stored as methods
class commands:
    def __init__(self):
        pass
    def fetch(symbols):
        stockJson = f.get(symbols)
        return str(stockJson)