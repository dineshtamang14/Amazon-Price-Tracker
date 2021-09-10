import requests
from bs4 import BeautifulSoup
import smtplib
from rupee import Rupee
import math

my_price = 24000
rupee = Rupee()
MY_EMAIL = "dineshshah960@gmail.com"
PASSWORD = "tamang12"
URL = "https://www.amazon.com/Realme-RMX3081-Factory-Unlocked-Infinito/dp/B093CBX4J6/ref=sr_1_3?dchild=1&keywords" \
      "=realme+8+pro&qid=1631263949&sr=8-3 "

headers_params = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 "
                  "Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5"
}

response = requests.get(URL, headers=headers_params)
data = response.text

soup = BeautifulSoup(data, "lxml")
product = soup.find(name="span", id="priceblock_ourprice").getText()

product_price = math.ceil(float(product.split("$")[1]) * rupee.current)
print(product_price)

if product_price <= my_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="dineshtamang7263@gmail.com", msg="subject: Amazon Price "
                                                                                           "Alert! "
                                                                                           "\n\n the price of your "
                                                                                           "product is very low now"
                                                                                           f"is below {my_price}"
                                                                                           f"visit this link:"
                                                                                           f"{URL} ")
