from unittest import result
import requests
from bs4 import BeautifulSoup
import pandas as pd
from itertools import chain


def get_page_links(url):
    baseurl = 'https://www.thewhiskyexchange.com/'
    r = requests.get(url)
    sp = BeautifulSoup(r.text, 'lxml')
    links = sp.select('li.product-grid__item a')
    return [baseurl + link.attrs['href'] for link in links]


def product_data(url):
    r = requests.get(url)
    sp = BeautifulSoup(r.text, 'lxml')
    product = {
        'title': sp.select_one('h1.product-main__name').text.strip().replace('\n', ''),
        'price': float(sp.select_one('p.product-action__price').text.strip().replace('£', '')),
        'stock': sp.select_one('p.product-action__stock-flag').text.strip().replace('\n', ''),
        'desc': sp.select_one('div.product-main__description p').text.strip().replace('\n', ''),
    }
    return product


def main():
    results = []
    for x in range(1, 3):
        urls = get_page_links(
            f'https://www.thewhiskyexchange.com/c/503/beer?pg={x}')
        productinfo = [product_data(url) for url in urls]
        results.append(productinfo)
        print(f'page {x} Completed.')
    return results


# print(main())
df = pd.DataFrame(list(chain.from_iterable(main())))
df.to_csv('world1.csv', index=False)
print("Save to CSV")
