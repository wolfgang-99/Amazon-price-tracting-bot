from bs4 import BeautifulSoup
import lxml
import requests
import smtplib

url = "https://www.amazon.com/Duo-Evo-Plus-esterilizadora-vaporizador/dp/B07W55DDFB/ref=sr_1_4?qid=1597660904 "
param= { 'Accept-Language' : "en-US,en;q=0.9",
        'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                       " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
title = "cooker"
target_price = "100"
YOUR_EMAIL = "python1email1@gmail.com"
YOUR_PASSWORD = "Abcd1234()"
YOUR_SMTP_ADDRESS = "smtp.gmail.com"
RECEVIER_EMAIL = "uaodhcxkn"

respond = requests.get(url, headers=param)
soup = BeautifulSoup(respond.text, "lxml")
price = soup.find(name="span", class_="a-price-whole")
#print(soup.prettify())
price = int(price.text)

if price <= 100 :
    message = f"{title} is now less {target_price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=RECEVIER_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )