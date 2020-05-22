# семинар 9 :)

import numpy as np
import pandas as pd

from scipy import stats # more style :)

import seaborn as sns
import matplotlib.pyplot as plt

plt.style.use('ggplot')  # стиль для графиков
%matplotlib inline

# Задачка 1

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



# А именно, величины $X_1$, ..., $X_{n}$ независимы и нормальны $N(0;1)$, 
# величины $Y_1$, ..., $Y_n$ независимы и нормальны $N(0;2)$. И пусть $n=200$.

# Винни-Пух правда этого ничего не знает, потому что у него в голове опилки, 
# и тестирует сначала гипотезу о равенстве дисперсий двух выборок на уровне значимости $5\%$.

# а) Проведите $10^6$ экспериментов, то есть $10^6$ раз попробуйте за Винни-Пуха проверить гипотезу

n_exp = 10 ** 6
n_obs = 200
# включаем логику: от экспериментов нам нужно только выборочное среднее и оценка дисперсии :)
# \bar X ~ N(0, 1/n_obs), \bar Y ~ N(0, 2/n_obs)
wp = pd.DataFrame({'xbar': stats.norm.rvs(loc=0, scale=np.sqrt(1 / n_obs), size=n_exp),
    'ybar': stats.norm.rvs(loc=0, scale=np.sqrt(2 / n_obs), size=n_exp)})

# продолжаем логику (чтобы сэкономить время в 200 раз :)
# \hat \sigma^2  ~ \chi^2_{n-1} * sigma^2 / (n - 1)
wp['xvar'] = stats.chi2.rvs(df=n_obs - 1, size=n_exp) * 1 / (n_obs - 1)
wp['yvar'] = stats.chi2.rvs(df=n_obs - 1, size=n_exp) * 2 / (n_obs - 1)

wp['f_stat'] = wp['xvar'] / wp['yvar']

sns.distplot(wp['f_stat'])

f_crit_right = stats.f.ppf(0.975, dfn=n_obs - 1, dfd=n_obs - 1)
f_crit_left = stats.f.ppf(0.025, dfn=n_obs - 1, dfd=n_obs - 1)
f_crit_left, f_crit_right

# б) Если гипотеза о равенстве дисперсий не отвергается, то Винни использует  
# t-статистику для проверки гипотезы о равенстве ожиданий при равенстве дисперсий.

wp_subset = wp.query('f_stat > @f_crit_left & f_stat < @f_crit_right')
wp_subset.head()
1 - wp_subset.shape[0] / n_exp

# https://en.wikipedia.org/wiki/Student%27s_t-test#Equal_or_unequal_sample_sizes,_similar_variances_(_%7F'%22%60UNIQ--postMath-00000011-QINU%60%22'%7F_%3C_%7F'%22%60UNIQ--postMath-00000012-QINU%60%22'%7F_%3C_2)
wp_subset['sigma_tot'] = np.sqrt(wp_subset['xvar'] * 0.5 + wp_subset['yvar'] * 0.5)
wp_subset['t_stat'] = (wp_subset['xbar'] - wp_subset['ybar']) / wp_subset['sigma_tot'] / np.sqrt(2 / n_obs)

sns.distplot(wp_subset['t_stat'])

t_crit_right = stats.t.ppf(0.975, df=2 * (n_obs - 1))
t_crit_left = - t_crit_right
t_crit_left, t_crit_right

wp_sub2 = wp_subset.query('t_stat > @t_crit_left & t_stat < @t_crit_right')
wp_sub2.shape[0]

1 - wp_sub2.shape[0] / wp_subset.shape[0]

# эта фактическая вероятность ошибки первого рода похожа на 0.06, а не на 0.05 :)
# это существенное отличие (~20%)
# вызвано тем, что t-test мы можем использовать когда дисперсии равны,
# а не когда гипотеза о равенстве дисперсий не отвергнута (!)
