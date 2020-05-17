import numpy as np
import pandas as pd

from scipy import stats

import seaborn as sns
import matplotlib.pyplot as plt

plt.style.use('ggplot')
%matplotlib inline


n_obs = 500

# подкидываем кубик с повторениями много раз
x = np.random.choice(np.arange(1,7), size=n_obs) 

# считаем кумулятивную сумму
x_cumsum = np.cumsum(x)
x_cumsum[:5]



diam = sns.load_dataset('diamonds')

# does not work!
d2 = (diam.groupby('cut')
    .assign(cumx = np.cumsum(diam['x'])))

df['no_csum'] = df.groupby(['name'])['no'].cumsum()

