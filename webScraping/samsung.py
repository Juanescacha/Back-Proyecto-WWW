import requests
from bs4 import BeautifulSoup 

def extraData():
    
    baseUrl = "https://www.samsung.com/co/offer/#offer_smartphone"

    response = requests.get(baseUrl)

    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup) 

    for div in soup.find_all("div", class_="co16-discover-column-new__columns-item swiper-slide"):
      print("===================")
      #print(div.find("div",class_="co16-discover-column-new__headline-wrapper").h3.string)
      #print(div.find("div",class_="co16-discover-column-new__description-wrapper").p.string)
      print(div.find("div",class_="co16-discover-column-new__cta-wrapper").a["href"])
      #print(div.find("div",class_="image image--main-loaded").img.get('src'))

extraData()