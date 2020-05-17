# байка про длинные и широкие таблицы :)

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats


# игрушечный пример широкой таблицы

toy_wide = pd.DataFrame({'id': range(0, 100),
    'x': stats.norm.rvs(size=100), 'y': stats.norm.rvs(size=100)})


toy_wide

# превратим "широкий" набор данных в "длинный":
toy_long = toy_wide.melt(id_vars='id')

toy_long
sns.lineplot(data=toy_long, x='id', y='value', hue='variable')


# "длинный" в "широкий"
toy_back = toy_long.pivot(index='id', columns='variable', values='value')
toy_back
toy_back.reset_index()





n_exp = 100 # число экспериментов
n_obs = 1000 # число подбрасываний кубика в эксперименте
exps_array = stats.randint.rvs(low=1, high=7, size=(n_obs, n_exp))
# можно np.random.choice()
exps = pd.DataFrame(exps_array)

exps['step'] = np.arange(0, n_obs) + 1
exps.head()

exps_long = exps.melt(id_vars='step', var_name='experiment')
exps_long['cum_sum'] = exps_long.groupby('experiment')['value'].cumsum()
exps_long.query('experiment == 2').head()

exps_long['cum_mean'] = exps_long['cum_sum'] / exps_long['step'] 

sns.lineplot(data=exps_long.query('experiment < 5'), x='step', y='cum_mean', hue='experiment')
plt.axhline(3.5, linestyle='dashed', color='c')
plt.ylabel('Накопленное среднее')
plt.xlabel('Число подбрасываний кубика')
plt.title('Сходимость к математическому ожиданию:')


# сходимость почти наверное (almost surely) и сходимость по вероятности (in probability)

# almost surely: 
# каждая траектория рано или поздно войдёт в рамки плюс-минус эпсилон от мат. ожидания
# (*) на самом деле не каждая, а с вероятностью один, но в быту "с вероятностью 1" означает каждая
# например, если я запущу на компе 1000 траекторий, то с вероятностью один все они по сильному збч должны войти в рамки

# in probability
# доля траекторий (от общего числа траекторий) входящих в рамки плюс-минус эпсилон стремится к единице

epsilon = 0.1
exps_long['in_bounds'] = (exps_long['cum_mean'] < 3.5 + epsilon) & (exps_long['cum_mean'] > 3.5 - epsilon)

step_summary = (exps_long.groupby('step')
    .agg(prop_inside = ('in_bounds', np.mean))
    .reset_index())

step_summary.head()

sns.lineplot(data=step_summary, x='step', y='prop_inside')
plt.ylabel('Доля экспериментов, со среднем около ожидания')
plt.xlabel('Число подбрасываний кубика')
plt.title('Иллюстрация к ЗБЧ в слабой форме')
