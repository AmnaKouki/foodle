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
    products = soup.find_all('div', class_='product-item-info')
    res = []
    for product in products:
        try:
            title = ' '.join(product.find(
                'a', class_='product-item-link').text.strip().split())
        except:
            title = ''
        try:
            price = product.find('span', class_='price').text.strip()
        except:
            price = ''
        try:
            link = product.find('a', class_='product-item-link').get('href')
        except:
            link = ''
        try:
            image = product.find(
                'img', class_='product-image-photo').get('src')
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


def aziza(query):
    query = query.replace(' ', '+')
    url = f'https://aziza.tn/fr/catalogsearch/result/index/?product_list_limit=36&q={query}'
    html = get_html(url)
    if html:
        return get_data(html)
