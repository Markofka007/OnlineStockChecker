from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
from termcolor import colored
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# mail client stuff
sender_email = ''  # SENDER EMAIL
rec_email = ''  # RECEIVER EMAIL
password = ''  # SENDER EMAIL PASSWORD
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(sender_email, password)


def send_email(product_name, product_url):
    mail_subject = f'{product_name}'
    mail_body = f'{product_url}'
    msg = f'Subject: {mail_subject}\n\n{mail_body}'
    server.sendmail(sender_email, rec_email, msg)


# google chrome driver (user agent)
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# url list
urls = {
    'bestbuy_3080': 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440',
    'bestbuy_3070': 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442'
}
site_list = ['BestBuy', 'BestBuy']
product_name = ['3080 Founders Edition', '3070 Founders Edition']
array_pointer = 0

print(colored(f'Now Testing [{len(urls)}] Sites', 'yellow'))

while True:
    array_pointer = 0
    for name, url in urls.items():
        driver.get(url)
        # print(driver.title)
        time.sleep(1)
        if "Sold Out" in driver.page_source:
            # print(f"{datetime.now()} <PST>: {driver.title}: {colored('Currently Sold Out', 'red')}")
            print(f"{colored(f'{datetime.now()}', 'white')}: {colored(f'[{site_list[array_pointer]}]', 'blue')} <{product_name[array_pointer]}>: {colored('CURRENTLY SOLD OUT', 'red')}")
            # send_email(f'{url_list[array_pointer - 1]} sold out :(', url)
        else:
            # print(f"{datetime.now()} <PST>: {driver.title}: {colored('CURRENTLY IN STOCK', 'green')}")
            print(f"{colored(f'{datetime.now()}', 'white')}: {colored(f'[{site_list[array_pointer]}]', 'blue')} <{product_name[array_pointer]}>: {colored('CURRENTLY SOLD OUT', 'red')}")
            # send_email(f'{name} IS BACK IN STOCK!!!', url)
        array_pointer = + 1
