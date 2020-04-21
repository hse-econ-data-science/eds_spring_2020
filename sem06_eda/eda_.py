# To add a new cell, type ''
# To add a new markdown cell, type '#'
#
# # <center> Exploratory Data Analysis </center>
#
# ## 1. Знакомство с библиотекой numpy
#
# **NumPy** — библиотека языка Python, позволяющая [удобно] работать с многомерными массивами и матрицами, содержащая математические функции. Кроме того, NumPy позволяет векторизовать многие вычисления, имеющие место в машинном обучении. 
# 
#  - [numpy](http://www.numpy.org)
#  - [numpy tutorial](http://cs231n.github.io/python-numpy-tutorial/)
#  - [100 numpy exercises](http://www.labri.fr/perso/nrougier/teaching/numpy.100/)
#  - [numpy data types](https://docs.scipy.org/doc/numpy/user/basics.types.html)


import numpy as np

#
# Основным типом данных NumPy является многомерный массив элементов одного типа — [numpy.ndarray](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.array.html). Каждый подобный массив имеет несколько *измерений* или *осей* — в частности, вектор (в классическом понимании) является одномерным массивом и имеет 1 ось, матрица является двумерным массивом и имеет 2 оси и т.д.
# 
# Создать массив из списков или кортежей можно с помощью функции ```np.array()```. 
# 
# ```np.array``` - функция, создающая объект типа ```np.ndarray```.


matrix = np.array([[1, 2, 3], [4, 5, 6]])
matrix



type(matrix)



matrix.ndim

#
# Чтобы узнать длину массива по каждой из осей, можно воспользоваться атрибутом ```shape```. Общее количество элементов выводим с помощью ```size```.


matrix.shape, matrix.size

#
# Альтернативные способы задать матрицу:


np.matrix('1 2; 3 4') # аргумент - строка или список



np.ndarray(shape=(3,3), dtype='float') # из случайных чисел

#
# Массивы специального вида можно создать при помощи функций zeros, ones, empty, identity:


np.zeros((3,))



np.ones((3, 4))



np.identity(3)



np.empty((2, 5))

#
# Еще можно создавать массивы при помощи функции arange:


np.arange(2, 20, 3)



np.arange(9)



np.arange(9).reshape(3, 3)

#
# Вместо значения длины массива по одному из измерений можно указать -1 — в этом случае значение будет рассчитано автоматически:


np.arange(8).reshape(2, -1)

#
# Теперь порешаем задачки!
# 
# **Задание 1.** Реализуйте функцию, возвращающую максимальный элемент в векторе x среди элементов, перед которыми стоит нулевой. Для x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0]) ответом является 5. Если нулевых элементов нет, функция должна возвращать None.


x = np.array([1, 5, 8, 6, 6, 1, 7, 4, 4, 0])

def max_element_before_zero(x):
    shift_by_one = np.hstack((1, x))
    bool_array = (shift_by_one == 0)[:np.size(shift_by_one) - 1]
    if np.size(x[bool_array]) == 0:
        return None
    else:
        return np.max(x[bool_array])
    
print ('Пример:', x, 'Максимальный элемент:', max_element_before_zero(x), sep='\n')
print ('Случайный вектор:', y, 'Максимальный элемент:', max_element_before_zero(y), sep='\n')

#
# **Задание 2.** Реализуйте функцию, принимающую на вход матрицу и некоторое число и возвращающую ближайший к числу элемент матрицы. Например: для X = np.arange(0,10).reshape((2, 5)) и v = 3.6 ответом будет 4.


def nearest_value(X, v):
    Y = np.abs(X - v)
    m = np.min(Y)
    inds = np.where(Y == m)
    return X[inds[0][0], inds[1][0]]

X = np.arange(0,10).reshape((2, 5))
v = 3.6
print ('Матрица:', X, 'Число:', v, 'Ближайший к числу элемент матрицы:', nearest_value(X, v), sep='\n')



# Решение в одну строку
def get_nearest_value(X, v):
    return int(np.min(np.abs(X - v)) + v)

print ('Матрица:', X, 'Число:', v, 
       'Ближайший к числу элемент матрицы:', get_nearest_value(X, v), sep='\n')

#
# **Задание 3.** Реализуйте функцию scale(X), которая принимает на вход матрицу и масштабирует каждый ее столбец (вычитает выборочное среднее и делит на стандартное отклонение). Убедитесь, что в функции не будет происходить деления на ноль. Протестируйте на случайной матрице (для её генерации можно использовать, например, функцию [numpy.random.randint](http://docs.scipy.org/doc/numpy/reference/generated/numpy.random.randint.html)).


def scale(X):
    std_deviation = X.std(axis=0)
    std_deviation[std_deviation == 0] = 1
    X = X - X.mean(axis=0) # или X -= X.mean(axis=0) c преобразованием X = X.astype(np.float)
    X /= std_deviation
    return(X)

X = np.random.randint(-7, 8, size=(2,5))
print ('Матрица:', X, 'Масштабированная матрица:', scale(X), sep='\n')

#
# ##  2. Pandas и первичный анализ данных
#
# **Pandas** (Python Data Analysis Library) — библиотека языка Python для удобных обработки и анализа данных.
#
# Небольшой список литературы:
# 
# 1. [Шпаргалка по pandas](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
# 
# 2. [Введение в pandas](https://khashtamov.com/ru/pandas-introduction/)
# 
# 3. [Статься в блоге сообщества OpenDataScience на Habr](https://habr.com/ru/company/ods/blog/322626/)
# 
# 4. [Туториалы в официальной документации (на английском)](https://pandas.pydata.org/docs/getting_started/10min.html)


import pandas as pd

#
# Качаем набор данных о футболистах из гитхаба курса, сохраняем в формате csv. Далее загружаем в Jupyter Notebook и внимательно указываем путь к файлу (в какие папки нужно перейти, чтобы увидеть файл).


df = pd.read_csv('data/data_football_profile.csv', sep='\t')



df.columns

#
# Функция возвращает DataFrame (то есть таблицу), однако затем приобретает ещё много важных параметров, среди которых:
# 
# * sep — разделитель данных, по умолчанию ',';
# * decimal — разделитель числа на целую и дробную часть, по умолчанию'.';
# * names — список с названиями колонок, не обязательный параметр;
# * skiprows — если файл содержит системную информацию, можно просто её пропустить. Необязательный параметр.
# 
# Дополнительные параметры можно посмотреть в [официальной документации.](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)
# 
# С помощью функции ```head``` можем посмотреть на первые несколько строк нашего датасета:


df.head()

#
# Удалим колонку Value, к которой мы не знаем точную интерпретацию:


df.drop(['Value'], axis=1, inplace=True)



# последние несколько строк:
df.tail(3)

#
# Посмотрим на размер нашего датасета. Первое число – количество строк (наблюдений), второе – количество столбцов (признаков):


df.shape

#
# Если вы хотите переименовать какую-то переменную, воспользуйтесь ```rename```:


df.rename({'Wage' : 'Salary'}, axis='columns', inplace=True)



df.columns

#
# Давайте посмотрим на информацию о датасете. В .info() можно передать дополнительные параметры, среди которых:
# 
# * verbose: печатать ли информацию о DataFrame полностью (если таблица очень большая, то некоторая информация может потеряться);
# * memory_usage: печатать ли потребление памяти (по умолчанию используется True, но можно поставить либо False, что уберёт потребление памяти, либо 'deep' , что подсчитает потребление памяти более точно);
# * null_counts: подсчитывать ли количество пустых элементов (по умолчанию True).


df.info()

#
# Можно вывести только тип данных в каждой колонке:


df.dtypes

#
# Метод describe показывает основные статистические характеристики данных по каждому числовому признаку (типы int64 и float64): число непропущенных значений, среднее, стандартное отклонение, диапазон, медиану, 0.25 и 0.75 квартили.


df.describe()

#
# Чтобы посмотреть статистику по нечисловым признакам (например, по строчным (object) или булевым (bool) данным), нужно явно указать интересующие нас типы в параметре метода describe include:


df.describe(include = ['object'])

#
# Выведем уникальные значения по возрасту и сколько раз каждое из них встречается в датасете (по убыванию). 


df['Age'].value_counts()

#
# Чтобы вывести уникальные значения в столбце или их количество, нужно использовать ```unique``` и ```nunique``` соответственно. Посмотрим, сколько у нас уникальных футбольных клубов. 


print('Всего {} футбольных клубов'.format(df['Club'].nunique()))



df['Club'].unique()[:10]

#
# Посчитаем арифметическое среднее, моду и медиану возраста футболистов (количественной переменной):


print('Среднее:', round(df['Age'].mean(), 2), 
      'Медиана:', df['Age'].median(), 
      'Мода:', df['Age'].mode()[0])

#
# Для качественных переменных с помощью pandas можно вывести моду. Посмотрим на самую часто встречающуюся национальность:


df['Nationality'].mode()

#
# Было бы полезно узнать, много ли у нас пропусков в датасете.


df.isna().sum()

#
# Чтобы удалить пропуски из данных, нужно вопспользоваться ```df.dropna()```, либо заполнить их значениями (например, средним) -  ```df.fillna(df['column_name'].mean())``` .
# Если в датасете содержатся дубликаты строк - воспользуйтесь методом ```df.drop_duplicates()```.


# заполним количественные переменные средними значениями (медианой)
for column in df.columns:
    if df[column].dtype != 'object':
        df[column] = df[column].fillna(df[column].median())
        
# у оставшихся переменных удалим строки с пропусками
df.dropna(inplace=True)

df.isna().sum()

#
# Часто возникает необходимость выбрать данные из DataFrame по определённому условию. Например, если в уже известном нам наборе данных о футболистах мы хотим выбрать только тех, у кого возраст больше 20 лет, используется следующий код:


df[df.Age > 20]

#
# **Задание:** Выберите футболистов, возраст которых больше среднего возраста футболистов, при условии, что они принадлежат ФК Барселона (Club == 'FC Barcelona').


df[(df.Age > df.Age.mean()) & (df.Club == 'FC Barcelona')]

#
# Чтобы объединить данные из нескольких датасетов по ключу (общей колонке), в pandas можно воспользовать встроенными аналогами SQL методов. В метод ```join``` в качестве аргумента how нужно указать тип объединения датасетов: inner, outer, left или right. 


# Вот так: 



df_info = pd.read_csv('data/data_football_info.csv', sep='\t')

joined_dfs = df_info.set_index('Name').join(df.set_index('Name'), how='inner').reset_index()
joined_dfs.head(5)




#animals.groupby("kind").agg(
#   ....:     min_height=('height', 'min'),
#   ....:     max_height=('height', 'max'),
#   ....:     average_weight=('weight', np.mean),
#   ....: )


#grouped.agg({'C': np.sum,
#   ....:              'D': lambda x: np.std(x, ddof=1)})



import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


df = sns.load_dataset('diamonds')


(df
 .filter(['carat', 'color'])
 .query('color == "E"')
 .head(3))


(df
 .filter(regex='^c')
 .query('cut in ["Ideal", "Premium"]')
 .groupby(['cut', 'color', 'clarity'])
 .agg(avgcarat=('carat', 'mean'), nobs=('carat', 'size'))
 .sort_values(by='avgcarat', ascending=False)
 .head())

b = (df
 .filter(regex='^c')
 .query('cut in ["Ideal", "Premium"]')
 .groupby(['cut', 'color', 'clarity'])
 .agg(avgcarat=('carat', 'mean'), nobs=('carat', 'size'))
 .reset_index()
 .sort_values(by='avgcarat', ascending=False))


c = b.reset_index()
c.head()


(df
 .assign(pricecat = pd.cut(df['price'], bins=3, labels=['low', 'med', 'high']))
 .filter(['x', 'z', 'pricecat'])
 .rename(columns={'x': 'width', 'z': 'depth'})
 .melt(id_vars=['pricecat'], value_vars=['width', 'depth'],
       var_name='dim', value_name='mm')
 .head())


df2 = (df
 .assign(pricecat = pd.cut(df['price'], bins=3, labels=['low', 'med', 'high']))
 .filter(['x', 'z', 'pricecat'])
 .rename(columns={'x': 'width', 'z': 'depth'})
 .melt(id_vars=['pricecat'], value_vars=['width', 'depth'],
       var_name='dim', value_name='mm')
 .query('2 < mm < 10'))

