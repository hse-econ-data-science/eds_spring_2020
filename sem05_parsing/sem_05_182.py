# парсинг

# Готовые таблички в html

url = 'https://ru.wikipedia.org/wiki/%D0%9F%D0%B0%D0%BD%D0%B4%D0%B5%D0%BC%D0%B8%D1%8F_COVID-19'

import pandas as pd 

all_tables = pd.read_html(url)

all_tables[3].head()

covid = all_tables[3]
covid.shape

covid.columns = ['junk', 'country',
    'infected', 'recovered', 'dead', 'mortality']

covid = covid.drop(columns='junk')

covid.head()
covid.tail()

covid = covid[:-1]
covid.describe()

# упражнение: отконвертируйте цифры в цифры :)
covid['mortality'] = pd.to_numeric(covid['mortality'])
covid.describe()

# упражнение: удалить почти пробелы :) из текста в столбце!
bad_sym = covid['infected'][0][3]
bad_sym
covid['infected'] = covid['infected'].str.replace(bad_sym, '')
covid['infected']

covid['infected'] = pd.to_numeric(covid['infected'])
covid.describe()

# попарсить просто страницу
import requests

url = 'http://books.toscrape.com/'

reply = requests.get(url)

reply.status_code
reply.headers
reply.headers['Last-Modified']
reply.content[:100]

from bs4 import BeautifulSoup

tree = BeautifulSoup(reply.content)

tree.html.head

all_a = tree.find_all('a')
a_ex = all_a[9]
a_ex
a_ex.text
a_ex.get_text()
a_ex.get_text().strip()
a_ex.get('href')

all_a = tree.find_all('a')
for a in all_a:
    print(a.get('href'))


all_books = tree.find_all('article')

book_ex = all_books[9]

book_ex

book_ex.h3.a.get_text() # title
book_ex.h3.a.get('href') # link
p = book_ex.find('p', {'class': 'price_color'})
p.get_text()[1:] # price
p1 = book_ex.find('p')
p1.get('class')[1] # rating

def get_page(url):
    reply = requests.get(url)
    tree = BeautifulSoup(reply.content)
    all_books = tree.find_all('article')

    books_data = [ ]
    for book in all_books:
        title = book.h3.a.get_text() # title
        link = book.h3.a.get('href') # link

        p = book.find('p', {'class': 'price_color'})
        price = p.get_text()[1:] # price

        p1 = book.find('p')
        rating = p1.get('class')[1] # rating
        books_data.append({'title': title,
            'link': link,
            'price': price,
            'rating': rating})
    return books_data

url = 'http://books.toscrape.com/catalogue/page-2.html'
bd = get_page(url)

books = pd.DataFrame(bd)
books['price'] = pd.to_numeric(books['price'])

books.describe()

# 1. Ищите готовые :)
# 2. Ищите API
# 3. bs / Scrapy
# 4. Selenium

# Selenium: кликаем по кнопочкам :)

from selenium import webdriver

ffox = webdriver.Firefox()

url = 'https://www.google.com/'
ffox.get(url)

search_field = ffox.find_element_by_name('q')
search_field.send_keys('вшэ')

search_button = ffox.find_element_by_name('btnK')
search_button.click()

tree = BeautifulSoup(ffox.page_source)
all_a = tree.find_all('a')
for a in all_a:
    print(a.get('href'))

ffox.close() # пусть Лисичка отдыхает :)

