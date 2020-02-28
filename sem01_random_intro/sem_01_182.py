import pandas as pd # работа с табличками
import numpy as np # математика с массивами
import seaborn as sns # графики
from scipy import special # спец функции
from scipy.stats import norm, expon, poisson, uniform

special.factorial(10) # 10!
special.binom(10, 5) # C_10^5

np.random.seed(777) # зерно генератора случайных чисел
x = norm.rvs(size=100, loc=5, scale=6) # N(5, 6^2)
x
y = uniform.rvs(size=100, loc=5, scale=6) # U[5, 11]
y 

z = [a for a in range(2, 15)]
z

z = [np.cos(a) for a in range(2, 15) if a > 6]
z

gorshok = pd.DataFrame({'gor': norm.rvs(size=100, loc=5, scale=6),
    'shok': uniform.rvs(size=100, loc=5, scale=6)})
gorshok

gorshok['gor'].mean()
gorshok['gor'].var()

gorshok.cov()
gorshok.corr()

gorshok.describe()


# P(N(5, 6^2) < 10)?
norm.cdf(10, loc=5, scale=6)

# P(N(5, 6^2) < a) = 0.05. a?
norm.ppf(0.05, loc=5, scale=6)


def udav(len_bulki=10):
    '''
    Симулятор нелёгкой судьбы удава Жоржа

    Args:
        len_bulki: длина булки (в метрах)
        
    Returns:
        int: число укусов на съедение булки
    '''
    bites = 0
    while len_bulki > 0:
        len_bulki -= uniform.rvs()
        bites += 1
    return bites

udav(len_bulki=8.7)


rdu = [udav(10) for a in range(10000)]
np.mean(rdu)

korzinka = pd.DataFrame({'x': rdu})
korzinka
korzinka['x3'] = korzinka['x'] ** 3

korzinka.describe()

sns.distplot(korzinka['x']) # гистограмма
sns.jointplot(data=gorshok, x='gor', y='shok') # диаграмма рассеяния

# если график не показывается, то вытаскиваем его на свет!
import matplotlib.pyplot as plt
plt.show()