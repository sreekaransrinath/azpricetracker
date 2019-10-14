import requests
from bs4 import BeautifulSoup   #Python library, to pull data out of HTML/XML files
import smtplib
import time

URL = input("Enter the Amazon URL here: ")
ideal_price = int(input("Enter the price you want it at: "))
emailid = input("Where do you want me to email you? ")
sender_email = input("Enter the email address from which the notification email is to be sent: ")
sender_pass = input("Enter the password for the email address from which the notification email is to be sent: ")
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
    subject = 'Price of your item has fallen!'
    body = 'The price of your item has fallen! Check the Amazon link for your amazing deal.'
    msg = "Subject: " + subject + "\n\n" + body + URL
    server.sendmail(sender_email, emailid, msg)
    print("Email has been sent!", msg)
    server.quit()

while (1):
    check_price()
    time.sleep(3600)
