# семинар 9 :)

import numpy as np
import pandas as pd

from scipy import stats # more style :)

import seaborn as sns
import matplotlib.pyplot as plt

plt.style.use('ggplot')  # стиль для графиков
%matplotlib inline

nod = pd.read_csv('nod_2020-05-17.csv')
nod.head()

nod.describe()

nod.groupby('group').agg(mean_kr1 = ('k1', np.mean)).reset_index()

# а) Постройте гистограмму результатов за первую контрольную, переменная `k1` :)
sns.distplot(nod['k1'])

sns.set_style({'font.family': 'serif', 'font.serif': 'Linux Libertine'})
sns.distplot(nod['k1'], kde=False)
plt.title('Гистограмма результатов за первую кр')
plt.xlabel('Результат в баллах')
plt.ylabel('Количество человек')

# б) Постройте примерный 95%-й доверительный интервал для ожидамоего результата за первую контрольную.
# центр интервала Y и se(Y)
# \bar X, se(\bar X) = \sqrt{\frac{\sum (X_i - \bar X)}{n-1}}
center = nod['k1'].mean()
center
se = nod['k1'].std() / np.sqrt(len(nod['k1']))
se
stats.norm.interval(0.95, loc=center, scale=se)

# puzzle
x = [0, 2]
np.var(x) # на что делит сумму np.var? на n или на (n-1)?
((0 - 1)^1 + (2 - 1)^2) / 2 = 1 # вывод: делит на n

varn = lambda x: np.sum((x - np.mean(x)) ** 2) / len(x)
varn1 = lambda x: np.sum((x - np.mean(x)) ** 2) / (len(x) - 1)
varn(x)
varn1(x)
np.var(x, ddof=1) # на что делит на (n-1) :)

varn2 = lambda x: np.var(x) * len(x) / (len(x) - 1)
varn2(x)

# магия!
nod.groupby('group').agg(raz1 = ('k1', np.var),
    raz2 = ('k1', varn), raz3 = ('k1', varn1), raz4 = ('k1', varn2),
    raz5 = ('k1', lambda x: np.var(x, ddof=1))).reset_index()

# какие выборычные дисперсии равны?


# Ангелы vs Демоны!
# type == "angel" / "demon"
nod['type'] = np.where(nod['d1fraud'] == 0, 'Angel', 'Demon')

angel_k1 = nod.query('type == "Angel"')['k1']
demon_k1 = nod.query('type == "Demon"')['k1']

sns.distplot(angel_k1, hist=False)
sns.distplot(demon_k1, hist=False)


sns.distplot(angel_k1, kde=False)
sns.distplot(demon_k1, kde=False)


# г) Постройте примерный 95%-й доверительный интервал для разницы ожидаемого результата за первую контрольную у Ангелов и Демонов. 
# Без предположения о равенстве дисперсий.
n_angel = len(angel_k1)
n_demon = len(demon_k1)

center = angel_k1.mean() - demon_k1.mean()
center
se = np.sqrt(angel_k1.var() / n_angel + demon_k1.var() / n_demon) # [упр]
se
# через asy normal
stats.norm.interval(0.95, loc=center, scale=se) # грубо без поправки Welch
# 0 in CI => H0 о равенстве ожиданий не отвергается

# через аппроксимацию t-распределением
stats.ttest_ind(angel_k1, demon_k1, equal_var=False) # аппроксимация Уэлча
stats.ttest_ind(angel_k1, demon_k1, equal_var=False, nan_policy='omit') # аппроксимация Уэлча
# pvalue=0.19 > alpha = 0.05 => H0 о равенстве ожиданий не отвергается

