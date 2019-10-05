import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = input("Enter the amazon URL here ")
ideal_price = int(input("Enter the price you want it at "))
emailid = input("Where do you want me to email you? ")
sender_email = xyz@gmail.com   #made by us
sender_pass = xyz              #made by us
headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="productTitle").get_text().strip()
    price = soup.find(id="priceblock_ourprice").get_text()
    price = int(price[2:4]+price[5:8])
    print(title, price)
    if (price <= ideal_price):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender_email, sender_pass)
    subject = 'Price Fell Down!'
    body = 'Price fell down! Check the amazon link'
    msg = "Subject: " + subject + "\n\n" + body + URL
    server.sendmail(sender_email, emailid, msg)
    print("email has been sent!", msg)
    server.quit()

while (1):
    check_price()
    time.sleep(3600)
