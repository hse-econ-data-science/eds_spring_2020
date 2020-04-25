# eda (exploratory data analysis)

import numpy as np
import pandas as pd
import seaborn as sns

# 1. загрузить локальный
data = pd.read_csv('...')
data = pd.read_excel('...')
data = pd.read_html('...')

# встроенный в seaborn
diam = sns.load_dataset('diamonds')

# 2. первый взгляд на структуру данных
diam.head()
diam.tail()
diam.shape
diam.isna().sum() # пропуска
diam.describe() # описательные статистики
diam.info()

diam.columns

# рекомендация: английский, одним словом, 
# маленькие буквы, без пробелов

# 3. отбор наблюдений
# упр: как мне отобрать бриллиаты с массой более 1 карата?
# вар 1.
diam2 = diam[diam['carat'] > 1]

import this
# вар 2. 
diam2b = diam.query('carat > 1 & price < 2500')

# 4. отбор переменных
# упр: отберите переменные cut, carat, clarity, color
diam2 = diam[['cut', 'carat', 'clarity', 'color']]

# вар 2. 
diam2b = diam.filter(['cut', 'carat', 'clarity', 'color'])

# регулярные выражение: 
# ^ - начало строки
# $ - конец строки
# | - или
diam2b = diam.filter(regex='^c')
diam2b.columns
# отберите столбцы, названия которых оканчиваются на e
diam2b = diam.filter(regex='e$')
# отберите столбцы, названия которых есть lo или la
diam2b = diam.filter(regex='lo|la')

# не брать столбец
diam2b = diam.drop(columns=['color', 'cut'])

# 5. сортировка наблюдений
# отсортируйте по убыванию цены
diam2 = diam.sort_values('price', ascending=False)

diam2.head()

# 6. переименовать переменную
diam2 = diam.rename(columns={'carat': 'weight'})
diam2.head(7)

# 7. создание новой переменной
# упр: создайте переменную ln_price с логарифмом цены

# вар 1.
diam['ln_price'] = np.log(diam['price'])
# вар 2.
diam2 = diam.assign(ln_price=np.log(diam['price']))

# вар 2 допускает комбо!
# комбо-цепочка:
# создайте лог цены, отберите ln_price > 6,
# отсортируйте по массе по возрастанию, выберите топ 5

# 8. комбо серии 
# лайфхак () довольно произвольно делать разрывы

diam2 = (diam
    .assign(ln_price=np.log(diam['price']))
    .query('ln_price > 6')
    .sort_values('carat', ascending=True)
    .head(5))

# упражнение
# сделайте комбо серию:
# - отсортируйте по убыванию размера x (мм)
# - взять нижние 100
# - создать переменную price2 = price^2
# - удалить все переменные кроме price и price2

diam2 = (diam
    .sort_values('x', ascending=False)
    .tail(100)
    .assign(price2=diam['price'] ** 2)
    .filter(['price', 'price2']))
diam2

# 9. группировка по переменным
# split - apply - combine strategy
# для каждого сочетания цвета и огранки посчитайте
# среднюю цену
# выборочное стандартное отклонение от массы
# сколько наблюдений входит в группу
diam2 = (diam
    .groupby(['cut', 'color'])
    .agg(av_price=('price', np.mean),
        std_carat=('carat', np.std),
        n_obs=('price', 'size')))
diam2.head(10)

diam2b = (diam
    .groupby(['cut', 'color'])
    .agg(av_price=('price', np.mean),
        std_carat=('carat', np.std),
        n_obs=('price', 'size'))
    .reset_index())
diam2b.head(10)

# комбо:
# - разбейте переменную price на 4 корзинки
# - для каждой корзинки цен
# - посчитайте: кол-во наблюдений, 
#               среднюю массу, стандартное отклонение массы
# на выходе: обычную табличку без мультииндекса по строкам

diam2 = (diam
    .assign(priceg=pd.cut(diam['price'], bins=4))
    .groupby('priceg')
    .agg(av_carat=('carat', np.mean),
        std_carat=('carat', np.std),
        nobs=('carat', 'size'))
    .reset_index())
diam2

(diam
    .assign(priceg=pd.cut(diam['price'], bins=4, 
        labels=['low', 'med-', 'med+', 'high']))
    .groupby('priceg')
    .agg(av_carat=('carat', np.mean),
        std_carat=('carat', np.std),
        nobs=('carat', 'size'))
    .reset_index())


