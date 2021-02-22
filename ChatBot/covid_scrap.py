import requests
from bs4 import BeautifulSoup


def scrap(country):
    url = "https://www.worldometers.info/coronavirus/country/" + country + "/"
    req = requests.get(url)
    bsObj = BeautifulSoup(req.text, "html.parser")
    # data = bsObj.find_all("div", class_="maincounter-number")
    data = bsObj.find_all("li", class_="news_li")

    return data[0].text.strip()
