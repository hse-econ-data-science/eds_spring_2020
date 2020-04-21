import requests

url = 'http://books.toscrape.com/'

reply = requests.get(url)

reply
reply.headers

reply.headers['Last-Modified']
reply.content[:100]


from bs4 import BeautifulSoup

tree = BeautifulSoup(reply.content)

title = tree.html.head.title
title.get_text()

all_a = tree.find_all('a')
all_a[:4]

a4 = all_a[4]
a4

a4.get_text()
a4.get_text().strip()

a4.get('href')

# первое достижение! достаём все ссылки со странички:
all_a = tree.find_all('a')
for a in all_a:
    print(a.get('href'))

# вопросы есть?

all_books = tree.find_all('article')
book4 = all_books[4]
book4.h3
book4.h3.a.get('href') # (!)
book4.h3.a.get('title') # (!)

book4.find('p', {'class': 'price_color'}).get_text()[1:] # (!)
book4.find('p').get('class')[1] # (!)


def parse_page(url):
    reply = requests.get(url)
    tree = BeautifulSoup(reply.content)
    all_books = tree.find_all('article')

    data = [ ]
    for book in all_books:
        link = book.h3.a.get('href') # (!)
        title = book.h3.a.get('title') # (!)

        price = book.find('p', {'class': 'price_color'}).get_text()[1:] # (!)
        rating = book.find('p').get('class')[1] # (!)
        data.append({'link': link, 'price': price, 'title': title, 
            'rating': rating})
    return data


url = 'http://books.toscrape.com/catalogue/page-2.html'
# список словарей!

import pandas as pd

books = pd.DataFrame(parse_page(url))

books
books.head()
books.tail()
books.describe()

import numpy as np

books['junk'] = np.nan
# упражнение: конвертируйте price в числа!
books['price'] = float(books['price']) # fails
books['price'] = pd.to_numeric(books['price']) # works!

books.describe()

books = books.drop(columns='junk')

# easy html tables!
url = 'https://en.wikipedia.org/wiki/2019%E2%80%9320_coronavirus_pandemic'

all_tables = pd.read_html(url)
# много мусорных табличек!
cv = all_tables[4]

cv.shape
cv.columns = ['junk', 'country', 'cases', 'deaths', 'recoveries', 'ref']
cv = cv.drop(columns='junk')

cv.head()
cv.tail()
cv = cv[:-2]
cv.tail()

# Selenium
# если нужно вводить данные в форму, а API нет
from selenium import webdriver

ffox = webdriver.Firefox()

url = 'https://www.google.com/'

ffox.get(url)

search_field = ffox.find_element_by_name('q')
search_field.send_keys('вшэ')

search_button = ffox.find_element_by_name('btnK')
search_button.click()

tree = BeautifulSoup(ffox.page_source)
ffox.close() # (!)


all_a = tree.find_all('a')
# ...

# Scrapy
