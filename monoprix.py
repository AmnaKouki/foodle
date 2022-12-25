import requests
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


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
    products = soup.find_all('li', class_='product_item')
    res = []
    for product in products:
        try:
            mainfacture = product.find(
                'div', class_='div_manufacturer_name').text.strip()
            product_title = product.find(
                'div', class_='product-title').text.strip()
            contenance = product.find(
                'div', class_='div_contenance').text.strip()
            title = mainfacture + ' ' + product_title + ' ' + contenance
        except:
            title = ''
        try:
            price = product.find('span', class_='price').text.strip().replace(
                'DT', '').replace(' ', '')
        except:
            price = ''
        try:
            link = product.find(
                'div', class_='product-title').find('a').get('href')
        except:
            link = ''
        try:
            image = product.find(
                'a', class_='product-thumbnail').find('img').get('src')
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


def monoprix(query):
    query = query.replace(' ', '+')
    url = f'https://courses.monoprix.tn/lac/jolisearch?page=1&s={query}'
    html = get_html(url)
    if html:
        return get_data(html)
