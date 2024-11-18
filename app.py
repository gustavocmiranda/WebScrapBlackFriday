import sqlite3
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

def create_connection(db_name = 'data/echo_pop.db'):
    conn = sqlite3.connect(db_name)
    return conn


def setup_database(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS prices (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   product_name TEXT,
                   price INTEGER,
                   timestamp TEXT
                   )                   
''')
    conn.commit()

def fetch_page(url: str):
    url = url
    return requests.get(url=url)


def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    product_name = soup.find('h1', class_ = 'ui-pdp-title').get_text()

    # Usando o método select() com o seletor CSS fornecido
    price = soup.select("#ui-pdp-main-container > div.ui-pdp-container__col.col-3.ui-pdp-container--column-center.pb-16 > div > div.ui-pdp-container__row.ui-pdp-with--separator--fluid.ui-pdp-with--separator--40-24 > div.ui-pdp-container__col.col-2.mr-24.mt-8 > div.ui-pdp-price.mt-16.ui-pdp-price--size-large > div.ui-pdp-price__main-container > div.ui-pdp-price__second-line > span > span > span.andes-money-amount__fraction")[0].get_text()

    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

    return {
        'product_name': product_name,
        'price': price,
        'timestamp': timestamp
    }

def save_to_database(conn, data):
    new_row = pd.DataFrame([data])
    new_row.to_sql('prices', conn, if_exists='append', index=False)

def save_to_dataframe(product_info, df):
    new_row = pd.DataFrame([product_info])
    df = pd.concat([df, new_row], ignore_index=True)
    return df

def retornar_menor_valor(conn):
    cursor = conn.cursor()
    cursor.execute(''' 
            SELECT MIN(price), timestamp FROM prices
    ''')
    result = cursor.fetchone()
    return result[0], result[1]


if __name__ == '__main__':
    conn = create_connection()
    setup_database(conn)

    url = 'https://www.mercadolivre.com.br/echo-pop-smart-speaker-amazon-cor-preto-c2h4r9/p/MLB23995388#polycard_client=search-nordic&wid=MLB3682804149&sid=search&searchVariation=MLB23995388&position=3&search_layout=grid&type=product&tracking_id=136767de-929b-4d4f-b8ae-96bdfa8df1c9'
    df = pd.DataFrame()
    while True:
        page_content = fetch_page(url = url)
        product = parse_page(page_content.text)


        menor_valor, menor_timestamp = retornar_menor_valor(conn)
        current_price = int(product['price'])
        if current_price < menor_valor:
            print('Menor preco detectado')
            menor_valor = current_price
            menor_timestamp = product['timestamp']
        else:
            print('menor preco é o antigo')

        save_to_database(conn, product)
        print('dados salvos')
        time.sleep(10)