import requests

def extracData():
    baseUrl = "https://www.samsung.com/co/offer/#offer_smartphones"
    
    response = requests.get(baseUrl)
    print(response.text)
    
extracData()