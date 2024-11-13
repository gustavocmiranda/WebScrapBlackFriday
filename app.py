import sqlite3
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

def create_connection(db_name = 'echo_pop.db'):
    conn = sqlite3.connect()
    cursor = conn

def fetch_page(url: str):
    url = url
    return requests.get(url=url)

def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    product_name = soup.find('h1', class_ = 'ui-pdp-title').get_text()
    prices = soup.find_all('span', class_ = 'andes-money-amount__fraction')
    old_price = prices[0].get_text()
    new_price = prices[1].get_text()
    parcelado_price = prices[2].get_text()

    timestamp = time.strftime('')

    return {
        'product_name': product_name,
        'old_price': old_price,
        'new_price': new_price,
        'parcelado_price': parcelado_price
    }

def save_to_dataframe(product_info, df):
    new_row = pd.DataFrame([product_info])
    df = pd.concat([df, new_row], ignore_index=True)
    return df

if __name__ == '__main__':
    url = 'https://www.mercadolivre.com.br/echo-pop-smart-speaker-amazon-cor-preto-c2h4r9/p/MLB23995388#polycard_client=search-nordic&wid=MLB3682804149&sid=search&searchVariation=MLB23995388&position=2&search_layout=grid&type=product&tracking_id=42336bbe-feed-40fc-b3d8-3a93081ffb7c'
    df = pd.DataFrame()
    while True:
        page_content = fetch_page(url = url)
        product = parse_page(page_content.text)
        df = save_to_dataframe(product_info=product, df=df)
        print(df)
        time.sleep(10)