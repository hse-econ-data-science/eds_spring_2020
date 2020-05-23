# sem 9

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats


nod = pd.read_csv('nod_2020-05-17.csv')
nod.head()

nod.describe()

nod.dropna(subset=['k1'], inplace=True)

# среднее по группам :)
nod.groupby('group').agg(mean_kr1 = ('k1', np.mean)).reset_index()

sns.distplot(nod['k1'], kde=False)

#               n велико | n мало
#   X_i ~ N        t~N         t
#   X_i не N        N          ?

n_obs = nod.shape[0]

mean_k1 = nod['k1'].mean() # bar X
se_k1 = nod['k1'].std() # hat sigma = se(X_i)

se_barx = se_k1 / np.sqrt(n_obs) # se(bar X)

# 1а

# центр плюс-минус критич * se(центр)
stats.norm.interval(0.95, loc=mean_k1, scale=se_barx)
# !
# в документации к функции альфа = уровень доверия
# в лекциях по статистике альфа = вер-ть ошибки первого рода
z_cr = stats.norm.ppf(0.975)
mean_k1 - z_cr * se_barx, mean_k1 + z_cr * se_barx

# 1б

nod['type'] = np.where(nod['d1fraud'] > 0, 'demon', 'angel')
nod.head()


nod.groupby('type').agg(mean = ('k1', np.mean),
    std = ('k1', np.std),
    n = ('k1', len))

# 1в

sns.distplot(nod.query('type == "demon"')['k1'])
sns.distplot(nod.query('type == "angel"')['k1'])

# 1г

mean_a = nod.query('type == "angel"')['k1'].mean() 
mean_b = nod.query('type == "demon"')['k1'].mean() 
var_a = nod.query('type == "angel"')['k1'].var() 
var_b = nod.query('type == "demon"')['k1'].var() 
n_a = nod.query('type == "angel"')['k1'].size 
n_b = nod.query('type == "demon"')['k1'].size

se_diff = np.sqrt(var_a / n_a + var_b / n_b)

# 1а

# центр плюс-минус критич * se(центр)
stats.norm.interval(0.95, loc=mean_a - mean_b, scale=se_diff)


# 1д

nod['type2'] = np.where(nod['d1fraud'] > 2.5, 'demon', 'angel')
nod.head()


nod.groupby('type2').agg(mean = ('k1', np.mean),
    std = ('k1', np.std),
    n = ('k1', len))

# 1е

# левое и правое критическое значение для F распределения:
stats.f.interval(0.95, dfn=n_a - 1, dfd=n_b - 1)

f_obs = var_a / var_b 
f_obs

# H0: дисперсии равны отвергается :)

nod.columns
nod2 = nod.filter(regex='^k1|type$')
corr_a = nod2.query('type == "angel"').corr()
corr_b = nod2.query('type == "demon"').corr()


sns.heatmap(corr_a, annot=True)

sns.heatmap(corr_b, annot=True)


# 2а
# думаем:
# bar X ~ N(0, 1/100)
# bar Y ~ N(0, 2/200)
nx = 100
ny = 200
n_exp = 10 ** 6

wp = pd.DataFrame(
    {'xbar': stats.norm.rvs(loc=0, scale=np.sqrt(1 / nx), size=n_exp),
    'ybar': stats.norm.rvs(loc=0, scale=np.sqrt(2 / ny), size=n_exp)})

# hat sigma^2 ~ chi^2 * sigma^2 / (n - 1)

wp['xvar'] = stats.chi2.rvs(df=nx - 1, size=n_exp) * 1 / (nx - 1)
wp['yvar'] = stats.chi2.rvs(df=ny - 1, size=n_exp) * 2 / (ny - 1)

wp.head()

wp['f_stat'] = wp['xvar'] / wp['yvar']

sns.distplot(wp['f_stat'])

f_cr_left, f_cr_right = stats.f.interval(0.95, dfn=nx - 1, dfd=ny - 1)

# отберём те эксперименты, где гипотеза о равенстве дисперсий не отвергнута
wp2 = wp.query('f_stat > @f_cr_left & f_stat < @f_cr_right')

wp2.shape
wp.shape

1 - wp2.shape[0] / n_exp
# (!) гипотеза H0 не верна и тест её поэтому часто отвергает


?stats.ttest_ind_from_stats

?stats.ttest_1samp
