# EDA!

import numpy as np # числовые массивы
import pandas as pd # таблички
import seaborn as sns # графики

diam = sns.load_dataset('diamonds')

# загружаем
df = pd.read_csv('путь')
df = pd.read_excel('...')
df = pd.read_html('...')

# быстрый взгляд
diam.head() # голова
diam.tail() # хвост
diam.shape
diam.describe()
diam.isna().sum() # пропуски

diam.columns
# стиль: маленькие буквы, по английски, без пробелов
diam.info()

# базовые операции с табличкой
# упр: отберите наблюдения в таблицу diam2
# критерий: цена бриллианта больше 1000

import this

# !! отбор наблюдений!
# вар 1:
diam2 = diam[diam['price'] > 1000]
diam2.shape

# вар 2:
diam2b = diam.query('price > 1000')
diam2b.shape
diam2b = diam.query('price > 1000 & color == "E"')

# !! отбор переменных!
# упр2: из diam отберите carat, cut, color, clarity
# вар1 
diam2 = diam[['carat', 'cut', 'color', 'clarity']]
diam2.shape

# удалить переменную: предпочитайте аргумент columns
# а не номер оси axis=2 для большей читабельности кода
diam2 = diam.drop(columns='carat')


# вар2
diam2b = diam.filter(['carat', 'cut', 'color', 'clarity'])

# регулярные выражение (!)
diam2b = diam.filter(regex='^c')
diam2b.columns
# упр: отберите переменные, заканчивающиеся на e
diam2b = diam.filter(regex='e$')
diam2b.columns

# ([A-Za-z]*)_([A-Za-z]*)_([A-Za-z-]*)_([0-9-]*)
# https://xkcd.com/208/


# !! сортировка наблюдений
# отсортируйте бриллианты по цене (по убыванию)
# вар1
diam2 = diam.sort_values('price', ascending=True)

# !! переименовать колонки
# упр. переименуйте carat в weight 
diam2 = diam.rename(columns={'weight': 'carat'})
diam2.columns

# !! создать новую переменную!
# упр: создайте логарифм цены ln_price
# вар1
diam['ln_price'] = np.log(diam['price'])

# вар2
diam2 = diam.assign(ln_price = np.log(diam['price']))
# длиннее? (-)
# можно строить цепочки (+)


# комбо: 
# создаю лог цены, фильтр лог > 6, сорт по массе, вывожу топ 5

# лайфхак! ()
diam2 = (diam
    .assign(ln_price = np.log(diam['price']))
    .query('ln_price > 6')
    .sort_values(by='carat')
    .head(5))

diam2

# split - apply - combine
# разделяй, влавствуй и соединяй!
# хочу по каждому цвету и качеству огранки посчитать:
# среднюю цену
# выбор ст. отклонение массы
# кол-во наблюдений

(diam
    .groupby(['cut', 'color'])
    .agg(av_price=('price', np.mean),
        std_carat=('carat', np.std),
        n_obs=('carat', 'size'))
    .reset_index())

# visual studio code
# shift + enter





