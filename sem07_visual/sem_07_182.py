import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

diam = sns.load_dataset('diamonds')
diam.head()

diam_small = diam.sample(n=100, random_state=777)
diam_med = diam.sample(n=1000, random_state=777)

# по быстрому!
sns.distplot(diam['carat'])

# тонкая настройка
sns.set_style({'font.family':'serif', 'font.serif':'Linux Libertine'})
hist = sns.distplot(diam['carat'], kde=False)
plt.title('Набор данных diamonds из пакета seaborn')
plt.xlim(0, 2.7)
plt.xlabel('Масса бриллианта [карат]')
plt.ylabel('Количество бриллиантов [тысяч]')
plt.suptitle('Распределение массы бриллиантов')
hist.axes.set_yticklabels([2, 4, 6, 8, 10, 12])

# критика:
# шрифт не соответствует основному тексту
# размер второй подписи поменьше

# с линией регрессии

sns.lmplot(data=diam_med, x='carat', y='price')

sns.jointplot(data=diam, x='carat', y='price', kind='hex')

# много наблюдений
sns.violinplot(data=diam, x='cut', y='price')

# мало наблюдений
sns.swarmplot(data=diam_small, x='cut', y='price')

# корреляционная матрица
corr_mat = diam.corr()
sns.heatmap(corr_mat, annot=True)

sns.catplot(data=diam_med, col='cut', x='clarity', y='price')

sns.catplot(data=diam, col='cut', x='clarity', y='price', kind='violin')

grid = sns.FacetGrid(data=diam, col='cut', row='clarity')
grid.map(plt.hist, 'carat')


sns.pairplot(diam_med.filter(['carat', 'x', 'price']))
sns.pairplot(diam_med.filter(['carat', 'x', 'price', 'cut']), hue='cut')

# широкий
# date | x | y | z
2020 | 5 | 7 | 13

# длинный
# date | variable | value
2020 | x | 5
2020 | y | 7
2020 | z | 13

from scipy.stats import norm

norm.rvs(size=100)

# широкий!
test = pd.DataFrame({'time': range(0, 100),
                    'x': norm.rvs(size=100),
                    'y': norm.rvs(size=100)})

test.head()

# длинный
test_long = pd.melt(test, id_vars='time')
test_long.head()

sns.lineplot(data=test_long, x='time', y='value', hue='variable')



