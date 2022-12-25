# https://www.geantdrive.tn/tunis-city/recherche?controller=search&orderby=price&orderway=asc&search_category=all&s=coca+cola&submit_search=

import requests
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# get html from url


def get_html(url):
    try:
        r = requests.get(url, verify=False)
        r.raise_for_status()
        return r.text
    except requests.exceptions.HTTPError as err:
        print(err)
        return None

# get data from html


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    products = soup.find_all('div', class_='item-product')
    res = []
    for product in products:
        try:
            name = product.find('h2', class_='product-title').find('a').text.strip()
            manif = product.find('p', class_='manufacturer_product').text.strip()
            desc = product.find('div', class_='product_short').text.strip()
            title = f'{name} {manif} {desc}'
        except:
            title = ''
        try:
            price = product.find('span', class_='price').text.strip().replace('DT', '').replace('\u00a0', '').replace(' ', '')
        except:
            price = ''
        try:
            link = product.find('a', class_='product-thumbnail').get('href')
        except:
            link = ''
        try:
            image = product.find('img', class_='img-responsive').get('src')
        except:
            image = ''
        data = {
            'title': title,
            'price': price,
            'link': link,
            'image': image,
        }
        res.append(data)
    return res


def geant(query):
    query = query.replace(' ', '+')
    url = f'https://www.geantdrive.tn/tunis-city/recherche?controller=search&orderby=price&orderway=asc&search_category=all&s={query}&submit_search='
    html = get_html(url)
    if html:
        return get_data(html)
