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
    # prices = soup.find_all('span', class_ = 'a-price-whole')
    # price = soup.find('span', class_= 'andes-money-amount__fraction').get_text()

    # Usando o método select() com o seletor CSS fornecido
    price = soup.select("#ui-pdp-main-container > div.ui-pdp-container__col.col-3.ui-pdp-container--column-center.pb-16 > div > div.ui-pdp-container__row.ui-pdp-with--separator--fluid.ui-pdp-with--separator--40-24 > div.ui-pdp-container__col.col-2.mr-24.mt-8 > div.ui-pdp-price.mt-16.ui-pdp-price--size-large > div.ui-pdp-price__main-container > div.ui-pdp-price__second-line > span > span > span.andes-money-amount__fraction")[0].get_text()

    parcelado_p = soup.find('p', id= 'pricing_price_subtitle')
    parcelado_price = parcelado_p.get_text()



    timestamp = time.strftime('')

    return {
        'product_name': product_name,
        'price': price,
        'parcelado': parcelado_price,
        'date': timestamp
    }

def save_to_dataframe(product_info, df):
    new_row = pd.DataFrame([product_info])
    df = pd.concat([df, new_row], ignore_index=True)
    return df

if __name__ == '__main__':
    url = 'https://www.mercadolivre.com.br/echo-pop-smart-speaker-amazon-cor-preto-c2h4r9/p/MLB23995388#polycard_client=search-nordic&wid=MLB3682804149&sid=search&searchVariation=MLB23995388&position=3&search_layout=grid&type=product&tracking_id=136767de-929b-4d4f-b8ae-96bdfa8df1c9'
    df = pd.DataFrame()
    while True:
        page_content = fetch_page(url = url)
        product = parse_page(page_content.text)
        df = save_to_dataframe(product_info=product, df=df)
        print(df)
        time.sleep(10)