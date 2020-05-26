import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from scipy.optimize import minimize


# 1a.
# f(x_1, x_2) = (x_1 - 2)^2 + (x_2 - 4)^2

def f1(x, y):
    z = (x - 2) ** 2 + (y - 4) ** 2
    return z

f1(3, 4)


def fun(theta):
    x, y = theta # распаковка параметров
    z = (x - 2) ** 2 + (y - 4) ** 2
    return z

fun([3, 4])

# mu, sigma = theta
# (y - mu) ** 2
# (y - theta[0]) ** 2

# алгоритмы оптимизации:
# - хотят производную
# - чихать на производную

theta_init = [0, 0]

opt_results = minimize(fun, theta_init)
opt_results

opt_results = minimize(fun, theta_init, method='nelder-mead')
opt_results

opt_results.x # точка минимума
opt_results.fun # значение функции
opt_results.status # 0 - критерий "успеха" алгоритма

# Теперь добавим в функцию параметр $a$: $f(x_1, x_2) = (x_1 - 2a)^2 + (x_2 - 4)^2$
# б) Найдите экстремум функции при $a=4$ и при $a=10$.

def fun(theta, a=1):
    x, y = theta # распаковка параметров
    z = (x - 2 * a) ** 2 + (y - 4) ** 2
    return z


theta_init = [0, 0]

opt_results = minimize(fun, theta_init, args=4)
opt_results

# $f(x_1, x_2, x_3) = 0.01 (x_1 - 0.5)^2 + |x_1^2 - x_2| + |x_1^2 - x_3|$
# устно? точка экстремума?

def bad_fun(x):
    return 0.01 * (x[0] - 0.5) ** 2 + abs(x[0] ** 2 - x[1]) + abs(x[0] ** 2 - x[2])

bad_fun([0.5, 0.25, 0.25])

x_init = [0, 0, 0]
opt_results = minimize(bad_fun, x_init)
opt_results # :()

x_init = [5, 0.25, 0.25]
opt_results = minimize(bad_fun, x_init, method='nelder-mead')
opt_results # :()


# визуализируем хорошую функцию :)
x = np.arange(-10, 10, 0.5)
y = np.arange(-10, 10, 0.5)
x
x_mesh, y_mesh = np.meshgrid(x, y) # сеточка
x_mesh

z_mesh = fun([x_mesh, y_mesh])
z_mesh # сетка значений фукнции

figure, axis = plt.subplots()
contour = axis.contour(x_mesh, y_mesh, z_mesh)
axis.clabel(contour, fontsize=8)
axis.set_title('График линий уровня функции fun')


# 3
fbock = pd.DataFrame({'y': [3.2, 7.9, 5.4, 4.9, 6.2, 4.3], 
    'ghost': [1, 2, 0, 0, 2, 0]})

# y - сколько коньяка выпила утром ФБ
# ghost - сколько приведений видела ФБ

# готовый метод максимального правдоподобия для некоторых распределений
stats.norm.fit(fbock['y']) # hat mu, hat sigma

# сделаем руками maxlik для Пуассона
# ghost_i ~ Poisson(rate), независимы

# P(ghost_i = k) = exp(-rate) * rate^k / k!
# ln P(ghost_i = k) = -rate + k ln(rate) - ln(k!)
# значения k_1, k_2, ..., k_n задаются выборкой! по ним нет оптимизации
# убрал ту часть, которая не влияет на экстремум
# ln P(ghost_i = k) = -rate + k ln(rate) 


# плохой стиль!
# в теории theta > 0, а оптимизатор не в курсе и может случайно перебрать theta < 0

# theta = интенсивность пуассоновского распределения
def neg_lklh(theta, fbock):
    ln_prob = -theta + fbock['ghost'] * np.log(theta)
    lklh = np.sum(ln_prob) # в силу независимости дней
    return -lklh

theta_init = 1 

opt_results = minimize(neg_lklh, theta_init, args=fbock)
opt_results

# правильный стиль = навесить преобразование 
# R -> (0; infty)
# R -> (0; 1)
# R -> (a; b)



# theta = логарифм интенсивность пуассоновского распределения
# theta = ln(rate)

def neg_lklh(theta, fbock):
    rate = np.exp(theta)
    ln_prob = -rate + fbock['ghost'] * np.log(rate)
    lklh = np.sum(ln_prob) # в силу независимости дней
    return -lklh

theta_init = -2

opt_results = minimize(neg_lklh, theta_init, args=fbock)
opt_results

np.exp(opt_results.x)


# пуассоновская регрессия
# rate_i = exp(a * 1 + b * y_i)
# ghost_i | rate_i ~ Poisson(rate_i)
# theta = (a, b)
def neg_lklh(theta, fbock):
    a, b = theta
    rate = np.exp(a + b * fbock['y'])
    ln_prob = -rate + fbock['ghost'] * np.log(rate)
    lklh = np.sum(ln_prob) # в силу независимости дней
    return -lklh

theta_init = [0, 0]

opt_results = minimize(neg_lklh, theta_init, args=fbock)
opt_results


# многие модели регрессии живут в statsmodels
import statsmodels.formula.api as smf

model = smf.poisson('ghost ~ 1 + y', data=fbock).fit()
model.summary()

