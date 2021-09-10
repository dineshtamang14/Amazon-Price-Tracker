import requests
from bs4 import BeautifulSoup


class Rupee:
    URL = "https://wise.com/in/currency-converter/usd-to-inr-rate?amount=1"
    response = requests.get(URL)
    data = response.text
    soup = BeautifulSoup(data, "html.parser")
    current = float(soup.find(name="span", class_="text-success").getText())
