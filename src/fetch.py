import requests
url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/auto-complete"

headers = {
    'x-rapidapi-key': "d81a20f172mshc140a4f4e3971fep1704cbjsn4df8c8a8184e",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
}

def get(ticker):
    query = {"q":ticker, "region":"US"}
    response = requests.request("GET", url, headers=headers, params=query)
    return response.text