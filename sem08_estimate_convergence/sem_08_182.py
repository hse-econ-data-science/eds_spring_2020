import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats


# если X_i независимы, одинаково распределены
# E(X_i) существует
# то:
# сильный ЗБЧ
# \bar X -> E(X_1) почти наверное (almost surely) (as)
# слабый ЗБЧ
# \bar X -> E(X_1) по вероятности (in probability) (p)

# эксперимент: кубик подбрасывается 500 раз
# проведем 100 экспериментов

n_exp = 100
n_obs = 500

# генерим подбрасывания (!)
# np.random # чуть быстрее
# stats.xxx.rvs # если нужны теоретические свойства (функция распредения и т.д.)

dice = stats.randint.rvs(low=1, high=7, size=(n_obs, n_exp))

dd = pd.DataFrame(dice)
dd['step'] = np.arange(1, n_obs + 1)
dd

# задача 1:
# Постройте график среднего для отдельного эксперимена
# по горизонтали: число подбрасываний
# по вертикали: текущее среднее

# переведём широкую таблицу в длинную
dd_long = dd.melt(id_vars='step', var_name='experiment')
dd_long

dd_long['sum'] = dd_long.groupby('experiment')['value'].cumsum()

dd_long.query('experiment == 7').head()

# упр 
# зная накопленную сумму (sum) и номер шага (step) посчитайте среднее
dd_long['mean'] = dd_long['sum'] / dd_long['step']

dd_subset = dd_long.query('experiment < 3')

sns.lineplot(x='step', y='mean', hue='experiment', data=dd_subset)
plt.axhline(3.5, linestyle='dashed', color='c')
plt.title('ЗБЧ в сильной форме:')


# сильный збч (almost surely)
# то: P(\bar X -> 3.5) = 1
# все три (любое конечное число) траектории сойдутся к 3.5 с вероятностью 1
# бытовым: все траектории, которые я увижу, сходятся к 3.5

# слабый збч (in probability)
# то: для любого eps > 0 оказывается, что P(|\bar X - 3.5| > eps) -> 0
 
eps = 0.1

dd_long['outside'] = abs(dd_long['mean'] - 3.5) > eps

dd_long

# упр. для каждого шага (step) посчитайте долю экспериментов 
# со средним лежащим от мат. ожидания дальше, чем на эпсилон
# 50000 * 6 столб -> 500 * 2 столб 
# на выходе:  step | prop_outside
#               1  |     1
#               2  |     0.99
# ...
#              100 |     0.05

step_summary = (dd_long.groupby('step')
    .agg(prop_outside=('outside', np.mean))
    .reset_index())

step_summary

sns.lineplot(data=step_summary, x='step', y='prop_outside')
plt.title('ЗБЧ в слабой форме:')


# упражнение три: у ЗБЧ есть предпосылки :)


# вместо кубика берём X_i ~ N(0, 1)
dice = stats.norm.rvs(loc=0, scale=1, size=(n_obs, n_exp))
dd = pd.DataFrame(dice)
dd['step'] = np.arange(1, n_obs + 1)

# переведём широкую таблицу в длинную
dd_long = dd.melt(id_vars='step', var_name='experiment')

dd_long['sum'] = dd_long.groupby('experiment')['value'].cumsum()

dd_long.query('experiment == 7').head()

dd_long['mean'] = dd_long['sum'] / dd_long['step']

dd_subset = dd_long.query('experiment < 3')

sns.lineplot(x='step', y='mean', hue='experiment', data=dd_subset)
plt.axhline(0, linestyle='dashed', color='c')
plt.title('ЗБЧ в сильной форме работает :)')

# вместо кубика берём X_i ~ t_1
dice = stats.t.rvs(df=1, size=(n_obs, n_exp))
dd = pd.DataFrame(dice)
dd['step'] = np.arange(1, n_obs + 1)

# переведём широкую таблицу в длинную
dd_long = dd.melt(id_vars='step', var_name='experiment')

dd_long['sum'] = dd_long.groupby('experiment')['value'].cumsum()

dd_long.query('experiment == 7').head()

dd_long['mean'] = dd_long['sum'] / dd_long['step']

dd_subset = dd_long.query('experiment < 3')

sns.lineplot(x='step', y='mean', hue='experiment', data=dd_subset)
plt.axhline(0, linestyle='dashed', color='c')
plt.title('ЗБЧ в сильной форме отдыхает :)')

# E(t_k) = 0 при k > 1 (!)
sns.distplot(dd_long.query('experiment == 0')['value'])

