# from dotenv import load_dotenv
# load_dotenv()
import price

from bs4 import BeautifulSoup
import requests
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time

chrome_options = Options()  
chrome_options.add_argument("--headless")  

driver=webdriver.Chrome(options=chrome_options)

base_url = 'https://www.kogan.com/nz/'
# token = os.getenv('TOKEN')
# chat_id = os.getenv('CHAT_ID')
token = price.TOKEN
chat_id = price.CHAT_ID
telegram_api = f'https://api.telegram.org/bot{token}/sendMessage'

items = [
    'buy/kogan-40-smart-full-hd-led-tv-android-tv-series-9-rf9220/',
    'buy/kogan-40-full-hd-led-tv-series-7-gf7400/'
]


for item in items:
    url = base_url + item
    driver.maximize_window()
    driver.get(url)
    
    time.sleep(0.2)
    content=driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content, 'html.parser')
    name = soup.find('h1', class_='_1BeEh').text.strip()
    price = soup.find('h5', class_='_3NZx-').text.strip()
    
    print(name, price)
    
    print(price)
    data = {
        'chat_id': chat_id,
        'text': f'*${price}*\n[{name}]({url})',
        'parse_mode': 'Markdown'
    }
    r = requests.post(telegram_api, data=data)

    ss
