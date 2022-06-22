from unittest import result
import requests
from bs4 import BeautifulSoup
from itertools import chain

url = 'https://monngonmoingay.com/tim-kiem-mon-ngon/'
r = requests.get(url)
html_contents = r.text
html_soup = BeautifulSoup(html_contents)
for found in html_soup.find_all(['a href']):
    print(found)
