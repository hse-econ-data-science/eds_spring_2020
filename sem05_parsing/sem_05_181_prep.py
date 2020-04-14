import requests  

url = 'http://books.toscrape.com/catalogue/page-1.html'
response = requests.get(url)
response


requests.get('http://books.toscrape.com/big_scholarship')


response.status_code
response.headers
response.headers['Last-Modified']

response.content[:100]


from bs4 import BeautifulSoup

# распарсили страничку в дерево 
tree = BeautifulSoup(response.content, 'html.parser')

title = tree.title
title
title.get_text()

all_a = tree.find_all('a')
a_example = all_a[7]
a_example.get_text()
a_example.get('href')

for a in all_a:
    print(a.get('href'))

b = tree.html.head.title.get_text()
b.strip()


books = tree.find_all('article')

books[0]

type(books[0])


books[0].find('p', {'class': 'price_color'}).get_text()[1:]

books[0].h3
books[0].h3.a.get('href')
books[0].h3.a.get('title')

# А ещё по этим атрибутам можно искать интересующие нас кусочки страницы. 
tree.find_all('a', {'title': 'A Light in the Attic'})


def get_page(p):
    
    # изготовили ссылку
    url = 'http://books.toscrape.com/catalogue/page-{}.html'.format(p)
    
    # сходили по ней
    response = requests.get(url)
    
    # построили дерево 
    tree = BeautifulSoup(response.content, 'html.parser')
    
    # нашли в нём всё самое интересное
    books = tree.find_all('article', {'class' : 'product_pod'})
    
    infa = [ ]
    
    for book in books:
        infa.append({'price': book.find('p', {'class': 'price_color'}).text,
                     'href': book.h3.a.get('href'),
                     'title': book.h3.a.get('title')})
                     
    return infa

infa = []

for p in range(1, 2):
    infa.extend(get_page(p))


import pandas as pd

df = pd.DataFrame(infa)
print(df.shape)
df.head()
df.describe()

# 
# * Слишком частые запросы раздражают сервер
# * Ставьте между ними временные задержки 

# %%
import time
time.sleep(3) # и пусть весь мир подождёт 3 секунды

# Запрос нормального человека через браузер выглядит так: 
# 
# <center>
# <img src="https://raw.githubusercontent.com/hse-econ-data-science/eds_spring_2020/master/sem05_parsing/image/browser_get.png" width="600"> 
#     
# С ним на сервер попадает куча информации! Запрос от питона выглядит так: 
# 
# 
# <center>
# <img src="https://raw.githubusercontent.com/hse-econ-data-science/eds_spring_2020/master/sem05_parsing/image/python_get.jpg" width="250"> 
#  
# Заметили разницу?  Очевидно, что нашему скромному запросу не тягаться с таким обилием мета-информации, которое передается при запросе из обычного браузера. К счастью, никто нам не мешает притвориться человечными и пустить пыль в глаза сервера при помощи генерации фейкового юзер-агента. Библиотек, которые справляются с такой задачей, существует очень и очень много, лично мне больше всего нравится [fake-useragent.](https://pypi.org/project/fake-useragent/) При вызове метода из различных кусочков будет генерироваться рандомное сочетание операционной системы, спецификаций и версии браузера, которые можно передавать в запрос:

# %%
from fake_useragent import UserAgent
UserAgent().chrome

# %% [markdown]
# Например, https://knowyourmeme.com/ не захочет пускать к себе python и выдаст ошибку 403. Она выдается сервером, если он доступен и способен обрабатывать запросы, но по некоторым личным причинам отказывается это делать.

# %%
url = 'https://knowyourmeme.com/'

response = requests.get(url)
response

# %% [markdown]
# А если сгенерировать User-Agent, вопросов у сервера не возникнет. 

# %%
response = requests.get(url, headers={'User-Agent': UserAgent().chrome})
response

# %% [markdown]
# __Другой пример:__ если захотите спарсить ЦИАН, он начнет вам выдавать капчу. Один из вариантов обхода: менять ip через тор. Однако на практически каждый запрос из-под тора, ЦИАН будет выдавать капчу. Если добавить в запрос `User_Agent`, то капча будет вылезать намного реже. 
# %% [markdown]
# ## в) общаться через посредников
# 
# <center>
# <img src="https://raw.githubusercontent.com/hse-econ-data-science/eds_spring_2020/master/sem05_parsing/image/proxy.jpeg" width="400"> 
# %% [markdown]
# Посмотрим на свой ip-адрес без прокси. 

# %%
r = requests.get('https://httpbin.org/ip')
print(r.json())

# %% [markdown]
# А теперь попробуем посмотреть, что будет если подключить прокси.

# %%
proxies = {
    'http': '182.53.206.47:47592',
    'https': '182.53.206.47:47592'
}

r = requests.get('https://httpbin.org/ip', proxies=proxies)

print(r.json())

# %% [markdown]
# Запрос работал немного подольше, ip адрес сменился. Большая часть проксей, которые вы найдёте работают криво. Иногда запрос идёт очень долго и выгоднее сбросить его и попробовать другую проксю. Это можно настроить опцией `timeout`.  Например, так если сервер не будет отвечать секунду, код упадёт. 

# %%
import requests
requests.get('http://www.google.com', timeout=1)

# %% [markdown]
# У requests есть довольно много разных интересных примочек. Посмотреть на них можно в [гайде из документации.](https://requests.readthedocs.io/en/master/user/advanced/)
# 
# 
# __Где можно попытаться раздобыть списки прокси:__ 
# 
# * https://qna.habr.com/q/591069
# * https://getfreeproxylists.blogspot.com/
# * Большая часть бесплатных прокси обычно не работает. Пишите парсер, который будет собирать списки из проксей и пытаться применить их. 
# %% [markdown]
# ## г) уходить глубже 
# 
# <center>
# <img src="https://raw.githubusercontent.com/hse-econ-data-science/eds_spring_2020/master/sem05_parsing/image/tor.jpg" width="600"> 
# 
# Можно попытаться обходить злые сервера через тор. Есть аж несколько способов, но мы про это говорить не будем. Лучше подробно почитать в нашей статье на Хабре. Ссылка на неё в конце тетрадки. Ещё в самом начале была. А ещё в середине [наверняка есть.](https://habr.com/ru/company/ods/blog/346632/)
# %% [markdown]
# ## Совместить всё? 
# 
# 1. Начните с малого 
# 2. Если продолжает банить, накидывайте новые примочки
# 3. Каждая новая примочка бьёт по скорости 
# 4. [Разные примочки для requests](http://docs.python-requests.org/en/v0.10.6/user/advanced/)
# %% [markdown]
# # 3. API 
# 
# __API (Application Programming Interface__ — это уже готовый код, который можно всунуть в свой код! Многие сервисы, в том числе Google и Вконтакте, предоставляют свои уже готовые решения для вашей разработки.
# 
# Примеры: 
# 
# * [Контактовский API](https://vk.com/dev/methods)
# * [API twitter](https://developer.twitter.com/en/docs.html) 
# * [API youtube](https://developers.google.com/youtube/v3/)
# * [API google maps](https://developers.google.com/maps/documentation/) 
# * [Aviasales](https://www.aviasales.ru/API)
# * [Yandex Translate](https://yandex.ru/dev/translate/)
# 
# Оно есть почти везде! На этом семинаре мы посмотрим на два примера: на API контакта и google maps.
# %% [markdown]
# ## 3.1 API vk
# 
# Зачем может понадобиться доступ к API контакта, думаю, объяснять не надо. Социальная сетка — это тонны различной полезной информации, которую можно заиспользовать для своего рисёрча. [В документации](https://vk.com/dev/manuals) очень подробно описано как можно работать с API контакта и к чему это приводит. 
# 
# Но для начала к API нужно получить доступ. Для этого придётся пройти пару бюрократических процедур (о, боже, эти два предложения были так бюрократически сформулированы, что мне захотелось отстоять в очереди).
# 
# Первая такая процедура заключается в создании своего приложения. Для этого переходим по [ссылке](http://vk.com/editapp?act=create) и проходимся по необходимым шагам:
# 
# <img align="center" src="https://raw.githubusercontent.com/hse-econ-data-science/eds_spring_2020/master/sem05_parsing/image/app_creation_1.png" width="500">
# 
# После подтверждения своей личности по номеру телефона, попадаем на страницу свежесозданного приложения
# 
# <img align="center" src="https://raw.githubusercontent.com/hse-econ-data-science/eds_spring_2020/master/sem05_parsing/image/app_creation_2.png" width="500">
# 
# Слева нам будем доступна вкладка с настройками, перейдя в неё мы увидим все необходимые нам для работы с приложением параметры:
# <img align="center" src="https://raw.githubusercontent.com/hse-econ-data-science/eds_spring_2020/master/sem05_parsing/image/app_creation_3.png" width="500">
# 
# Отсюда в качестве токена можно забрать сервисный ключ доступа. Для работы с частью методов API этого вполне достаточно (обычно в заголовке такого метода стоит соответствующая пометка). Иногда нужны дополнительные доступы. Для того, чтобы получить их, необходимо сделать ещё пару странных манипуляций:
# 
# Переходим по ссылке вида (на месте звездочек должен стоять ID созданного вами приложения):
# 
# > https://oauth.vk.com/authorize?client_id=**********&scope=8198&redirect_uri=https://oauth.vk.com/blank.html&display=page&v=5.16&response_type=token
# 
# В итоге по этому запросу будет сформирована ссылка следующего вида:
# > https://oauth.vk.com/blank.html#access_token=25b636116ef40e0718fe4d9f382544fc28&expires_in=86400&user_id=*******
# 
# Первый набор знаков — `access token`, т.е. маркер доступа. Вторая цифра (`expires_in=`) время работы маркера доступа в секундах (одни сутки). По истечению суток нужно будет получить новый маркер доступа. Последняя цифра (`user_id=`) ваш ID Вконтакте. Нам в дальнейшем понадобится маркер доступа. Для удобства сохраним его в отдельном файле или экспортируем в глобальную область видимости. В целях безопасности ваших данных не стоит нигде светить токенами и тем более выкладывать их в открытый доступ. __Так можно и аккаунта случайно лишиться.__ Берегите токен смолоду. 
# 
# Обратите внимание на ссылку, по которой мы делали запрос на предоставление токена. Внутри неё находится странный параметр `scope=8198.` Это мы просим доступ к конкретным разделам. Подробнее познакомиться с взаимно-однозначным соответствием между числами и правами можно [в документации.](https://vk.com/dev/permissions) Например, если мы хотим получить доступ к друзьям, фото и стенам, мы подставим в scope цифру 2+4++8192=8198.
# %% [markdown]
# На всякий случай вот гифки со всеми действиями. На левой начало, на правой конец (да, я знаю, что эти две гифки получились не самыми удачными, сори).  
# 
# <table>
# <tr>
# <td><img src="https://raw.githubusercontent.com/FUlyankin/Parsers/master/gifs/vk1.gif" width="550"> </td>
# <td><img src="https://raw.githubusercontent.com/FUlyankin/Parsers/master/gifs/vk2.gif" width="550"> </td>
# </tr>
# </table>

# %%
# мой номер странички
myid = '6045249'  # вставить номер странички

# версия используемого API
version = '5.103' 

# подгружаем токен из файлика на компьютере
with open('secret_token.txt') as f:
    token = f.read()

# %% [markdown]
# Чтобы скачать что-то из контакта, надо сделать ссылку и сходить по ней пакетом `requests`. Ссылка должна будет включать в себя метод (что мы просим у вк) и параметры (насколько много и как именно). Мы будем просто заменять эти две штуки и выкачивать разные вещи. 

# %%
method = 'users.get'
parameters = 'user_ids=6045249'

url = 'https://api.vk.com/method/' + method + '?' + parameters + '&v=' + version + '&access_token=' + token

response = requests.get(url) 
response.json()

# %% [markdown]
# В ответ на наш запрос vk выкидывает JSON с информацией. JSON очень похож на птонячие словарики. Смысл квадратных и фигурных скобок такой же. Правда, есть и отличия: например, в Python одинарные и двойные кавычки ничем не отличаются, а в JSON можно использовать только двойные. 
# 
# Мы видим, что полученный нами JSON представляет собой словарь, значения которого — строки или числа, а также списки или словари, значения которых в свою очередь также могут быть строками, числами, списками, словарями и т.д. То есть получается такая довольно сложная структура данных, из которой можно вытащить всё то, что нас интересует. 

# %%
response.json()['response'][0]['first_name']

# %% [markdown]
# [В документации](https://vk.com/dev/manuals) очень подробно описано какие есть методы и какие у них бывают параметры.  Давайте завернём код выше в функцию и попробуем что-нибудь скачать.

# %%
def vk_download(method, parameters):
    
    url = 'https://api.vk.com/method/' + method + '?' + parameters + '&access_token=' + token + '&v=' + version
    response = requests.get(url) 
    infa = response.json()
    return infa

# %% [markdown]
# Например, все лайки с [хайер скул оф мемс.](https://vk.com/hsemem)

# %%
group_id = '-139105204'  # взяли из ссылки на группу


# %%
wall = vk_download('wall.get', 'owner_id={}&count=100'.format(group_id))
wall = wall['response']


# %%
wall['items'][0]


# %%
wall['items'][0]['likes']['count']


# %%
likes = [item['likes']['count'] for item in wall['items']]
likes[:10]

# %% [markdown]
# За один запрос скачалось всего-лишь $100$ постов с лайками. В паблике их целых

# %%
wall['count']

# %% [markdown]
# [Документация](https://vk.com/dev/manuals) говорит, что есть параметр `offset`, с помощью которого можно указать какие именно посты из группы нужно скачать. Например, если мы укажем `offset = 100`, скачается вторая сотня. Наше дело за малым: написать цикл. 

# %%
import time

likes = [ ] # сюда буду сохранять лайки

for offset in range(0, 4800, 100):
    
    time.sleep(0.4) # вк согласен работать 3 раза в секунду, 
                    # между запросами python спит 0.4 секунды
    
    wall = vk_download('wall.get', 'owner_id={}&count=100&offset={}'.format(group_id, offset))
    
    likes.extend([item['likes']['count'] for item in wall['response']['items']])

# %% [markdown]
# Лайки в наших руках. Можем даже посмотреть на их распределение и попробовать что-то с ними сделать. 

# %%
len(likes)


# %%
import matplotlib.pyplot as plt 
plt.hist(likes);

# %% [markdown]
# В принципе похожим образом можно скачать что угодно. Обратите внимание, что у вк есть специальный метод [`execute`,](https://vk.com/dev/execute) который иногда помогает ускорить скачку в $25$ раз. [В этом очень старом туториале](https://github.com/DmitrySerg/OpenData/blob/master/RussianElections2018/Part_1_Parsing_VK.ipynb) даже есть пример использования. 
# %% [markdown]
# ## 3.2 API Google maps
# 
# API для карт может понадобиться для различных полугеографических исследований. Например, мы хотим проверить гипотезу о том, что хороший кофе повышает цену квартиры. Одним из регрессоров хотим взять число кофеен в окрестностях. Это количество кофеен надо откуда-то взять. Google maps вам в помощь! 
# 
# Снова всё начинается с [получения ключа.](https://developers.google.com/maps/documentation/directions/start) Тут всё намного проще. Переходим по ссылке, жмём Get started, соглашаемся со всем, кроме оплаты. Получаем ключ доступа, сохраняем его в файлик рядом с блокнотом. 

# %%
# подгружаем токен
with open('google_token.txt') as f:
    google_token = f.read()

# %% [markdown]
# Формируем ссылку для запроса по заветам [документации](https://developers.google.com/maps/documentation) и получаем ответ в виде JSON. 

# %%
mainpage = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'

location = '55.86,37.54'
radius = '3000'
keyword = 'кофейня'

parameters = 'location='+location+'&radius='+radius+'&keyword='+keyword+'&language=ru-Ru'+'&key='+ google_token

itog_url = mainpage + parameters 
itog_url


# %%
response = requests.get(itog_url)

response.json()['results'][0]

# %% [markdown]
# Из json по сотвествующим ключам тащим самое интересное. Например, названия заведений: 

# %%
[item['name'] for item in response.json()['results']]

# %% [markdown]
# [В этом старом недописанном гайде](https://nbviewer.jupyter.org/github/FUlyankin/Parsers/blob/master/Parsers%20/Google_maps_API.ipynb) есть ещё пара примеров по работе с google maps. 
# %% [markdown]
# # 4. Selenium
# 
# Это инструмент для роботизированного управления браузером. Для его коректной работы нужно скачать драйвер: [для хрома](https://sites.google.com/a/chromium.org/chromedriver/downloads) или [для фаерфокса.](https://github.com/mozilla/geckodriver/releases) 

from selenium import webdriver

driver = webdriver.Firefox()

ref = 'http://google.com'
driver.get(ref)

stroka = driver.find_element_by_name("q")
stroka.click()

stroka.send_keys('Вконтакте')

button = driver.find_element_by_name('btnK')
button.click()

bs = BeautifulSoup(driver.page_source)

dirty_hrefs = bs.find_all('h3',attrs={'class':'r'})
clean_hrefs = [href.a['href'] for href in dirty_hrefs]
clean_hrefs

driver.close()

# %% [markdown]
# Вообще selenium придумывали для тестировщиков, а не для парсинга. Для парсеров имеет смысл использовать только в крайнем случае. Он очень медленный. Если у вас очень-очень-очень-очень не получается обмануть сервер через requests или вы сталкиваетесь с какой-то специфической защитой от ботов, seleium может помочь. Ещё для selenium __важно__ не забывать ставить временные задержки, чтобы страница успевала прогрузиться. Либо можно дописывать полноценные код, который будет ждать прогрузки и только тогда тыкать на кнопки и тп. 
# 
# [В очередном старом гайде](https://nbviewer.jupyter.org/github/FUlyankin/Parsers/blob/master/sems/3_Selenium_and_Tor/4.1%20Selenium%20.ipynb) одного из семинаристом можно почитать чуть подробнее. Кроме того, есть [перевод на русский документации на хабре.](https://habr.com/ru/post/248559/)
# 
# В моей практике полезен был пару раз: 
# 
# * Надо было скачать много инфы о поисковых запросах из [Google Trends,](https://trends.google.ru/trends/?geo=RU) а API сильно ограничивал меня.
# * Надо было понять через поисковик какой у различных организаций ИНН по их наименованию (помогло только для крупных компаний) 
# %% [markdown]
# # 5. Хитрости: 
# 
# ### Хитрость 1:  Не стесняйтесь пользоваться `try-except`
# 
# Эта конструкция позволяет питону в случае ошибки сделать что-нибудь другое либо проигнорировать её. Например, мы хотим найти логарифм от всех чисел из списка: 

# %%
from math import log 

a = [1,2,3,-1,-5,10,3]

for item in a:
    print(log(item))

# %% [markdown]
# У нас не выходит, так как логарифм от отрицательных чисел не берётся. Чтобы код не падал при возникновении ошибки, мы можем его немного изменить: 

# %%
from math import log 

a = [1,2,3,-1,-5,10,3]

for item in a:
    try:
        print(log(item))  # попробуй взять логарифм
    except:
        print('я не смог') # если не вышло, сознайся и работай дальше

# %% [markdown]
# __Как это использовать при парсинге?__  Интернет создаёт человек. У многих людей руки очень кривые. Предположим, что мы на ночь поставили парсер скачивать цены, он отработал час и упал из-за того, что на како-нибудь одной странице были криво проставлены теги, либо вылезло какое-то редкое поле, либо вылезли какие-то артефакты от старой версии сайта, которые не были учтены в нашем парсере. Гораздо лучше, чтобы код проигнорировал эту ошибку и продолжил работать дальше. 
# %% [markdown]
# ### Хитрость 2:  pd.read_html
# 
# Если на странице, которую вы спарсили, среди тэгов `<tr>` и `<td>` прячется таблица, чаще всего можно забрать её себе без написания цикла, который будет перебирать все стобцы и строки. Поможет в этом `pd.read_html`. Например, вот так можно забрать себе [табличку с сайта ЦБ](https://cbr.ru/currency_base/daily/) 

import pandas as pd

all_df = pd.read_html('https://en.wikipedia.org/wiki/2019%E2%80%9320_coronavirus_pandemic')
cor_total = all_df[4]
cor_total.columns = ['a', 'b', 'c', 'd', 'e', 'f']
cor_total.head()
cor_total.tail()
cor_total = cor_total[:-2]

cor_total = cor_total.drop(columns='a')


df = pd.read_html('https://cbr.ru/currency_base/daily/', header=-1)[0]
df.head()

# %% [markdown]
# Команда пытается собрать в массив все таблички c веб-страницы. Если хочется, можно сначала через bs4 найти нужную таблицу, а потом уже распарсить её: 

# %%
resp = requests.get('https://cbr.ru/currency_base/daily/')
tree = BeautifulSoup(resp.content, 'html.parser')

# нашли табличку
table = tree.find_all('table', {'class' : 'data'})[0]

# распарсили её
df = pd.read_html(str(table), header=-1)[0]
df.head()

# %% [markdown]
# ### Хитрость 3:  используйте пакет tqdm
# 
# > Код уже работает час. Я вообще без понятия когда он закончит работу. Было бы круто узнать, сколько ещё ждать... 
# 
# Если в вашей голове возникла такая мысль, пакет `tqdm` ваш лучший друг. Установите его: ```pip install tqdm```

# %%
from tqdm import tqdm_notebook

a = list(range(30))

# 30 раз будем спать по секунде
for i in tqdm_notebook(a):
    time.sleep(1)

# %% [markdown]
# Мы обмотали тот вектор, по которому идёт цикл в `tqdm_notebook`. Это даёт нам красивую зелёную строку, которая показывает насколько сильно мы продвинулись по коду. Обматывайте свои самые большие и долгие циклы в `tqdm_notebook` и всегда понимайте сколько осталось до конца. 
# %% [markdown]
# ### Хитрость 4:  распаралеливание
# 
# Если сервер не очень настроен вас банить, можно распаралелить свои запросы к нему. Самый простой способ сделать это — библиотека `joblib`. 

# %%
from joblib import Parallel, delayed
from tqdm import tqdm_notebook

def simple_function(x):
    return x**2


nj = -1 # паралель на все ядра 
result = Parallel(n_jobs=nj)(
                delayed(simple_function)(item)          # какую функцию применяем 
                for item in tqdm_notebook(range(10)))   # к каким объектам применям

# tqdm_notebook в последней строчке будет создавать зелёный бегунок с прогрессом

# %% [markdown]
# На самом деле это не самый эффективный способ паралелить в python. Он жрёт много памяти и работает медленнее, чем [стандартный multiprocessing.](https://docs.python.org/3/library/multiprocessing.html) Но зато две строчки, КАРЛ! Две строчки! 
# %% [markdown]
# ### Хитрость 5:  selenium без браузера
# 
# Селениум можно настроить так, чтобы физически браузер не открывался.

# %%
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True 
driver = webdriver.Firefox(options=options)

ref = 'http://google.com'
driver.get(ref)

driver.close()

# %% [markdown]
# ###  Ещё хитрости: 
# 
# * __Сохраняйте то, что парсите по мере скачки!__ Прямо внутрь цикла запихните код, который сохраняет файл! 
# * Когда код упал в середине списка для скачки, не обязательно запускать его с самого начала. Просто сохраните тот кусок, который уже скачался и дозапустите код с места падения.
# * Засовывать цикл для обхода ссылок внутрь функции - не самая хорошая идея. Предположим, что надо обойти $100$ ссылок. Функция должна вернуть на выход объекты, которые скачались по всему этому добру. Она берёт и падает на $50$ объекте. Конечно же то, что уже было скачано, функция не возвращает. Всё, что вы накачали - вы теряете. Надо запускать заново. Почему? Потому что внутри функции своё пространство имён. Если бы вы делали это циклом влоб, то можно было бы сохранить первые $50$ объектов, которые уже лежат внутри листа, а потом продолжить скачку. 
# * Можно ориентироваться на html-страничке с помощью `xpath`. Он предназначен для того, чтобы внутри html-странички можно было быстро находить какие-то элементы. [Подробнее можно почитать тут.](https://devhints.io/xpath)
# * Не ленитесь листать документацию. Из неё можно узнать много полезных штук. 
# %% [markdown]
# # 6. Почиташки
# 
# * [Парсим мемы в python](https://habr.com/ru/company/ods/blog/346632/) - подробная статья на Хабре, по которой можно научиться ... парсить (ВНЕЗАПНО) 
# * [Тетрадки Ильи Щурова](https://github.com/ischurov/pythonhse) про python для анализа данных. В [лекции 9](https://nbviewer.jupyter.org/github/ischurov/pythonhse/blob/master/Lecture%209.ipynb) и [лекции 10](https://nbviewer.jupyter.org/github/ischurov/pythonhse/blob/master/Lecture%2010.ipynb) есть про парсеры. 
# * [Книга про парсинг](https://github.com/FUlyankin/Parsers/blob/master/Ryan_Mitchell_Web_Scraping_with_Python-_Collecting_Data_from_the_Modern_Web_2015.pdf) на случай если вам совсем скучно и хочется почитать что-то длинное и на английском
# * [Продвинутое использование requests](https://2.python-requests.org/en/master/user/advanced/)
# * [Перевод документации по selenium на русский на хабре](https://habr.com/ru/post/248559/)
# 
# 
# * [Страничка с парсерами одного из семинаристов,](https://fulyankin.github.io/Parsers/) на ней много недописанного и кривого, но есть и интересное: 
#     * [Более подробно про selenium](https://nbviewer.jupyter.org/github/FUlyankin/Parsers/blob/master/sems/3_Selenium_and_Tor/4.1%20Selenium%20.ipynb)
#     * [Немного устаревший гайд по парсинг вконтакте](https://nbviewer.jupyter.org/github/FUlyankin/ekanam_grand_research/blob/master/0.%20vk_parser_tutorial.ipynb)
#     * [Немного устаревший гайд про google maps](https://nbviewer.jupyter.org/github/FUlyankin/Parsers/blob/master/Parsers%20/Google_maps_API.ipynb)
# 
# 
# %% [markdown]
#    
