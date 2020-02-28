import numpy as np # массивы
import pandas as pd # таблички с данными
import seaborn as sns # графики
import matplotlib.pyplot as plt

from scipy import special
from scipy.stats import norm, expon, uniform

special.factorial(10)
special.binom(10, 5)


np.random.seed(seed=777) # инициализировали гсч
x = norm.rvs(size=100, loc=10, scale=7)
x

y = uniform.rvs(size=100, loc=5, scale=13)
y

z = [a for a in range(2, 21)]
z

z = [a for a in range(2, 21) if a > 5]
z

gorshok = pd.DataFrame({'gor': norm.rvs(size=100, loc=0, scale=5),
    'shok': expon.rvs(size=100, scale=7)})

gorshok.head()

gorshok.describe()
gorshok.cov()
gorshok.corr()

gorshok['dub'] = gorshok['gor'] * gorshok['shok']
gorshok.describe()

sns.distplot(gorshok['gor'])
plt.show()
sns.jointplot(data=gorshok, x='gor', y='shok')


def udav(len_bulki=1):
    '''
    Симулятор жизни удава Анатолия

    Args:
        len_bulki: длина булки

    Return: 
        int: число укусов булки
    '''
    bites = 0
    while len_bulki > 0:
        len_bulki -= uniform.rvs()
        bites += 1
    return bites

udav(10)
udav()

terra = [udav(10) for i in range(1000)]

np.mean(terra)
np.var(terra)