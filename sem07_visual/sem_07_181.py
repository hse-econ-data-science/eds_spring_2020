import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


diam = sns.load_dataset('diamonds')

diam_small = diam.sample(n=70, random_state=777)
diam_medium = diam.sample(frac=0.05, random_state=777)

# по быстрому!
sns.distplot(diam['carat'])

# много времени на настройку:
sns.distplot(diam['carat'])
plt.title('Распределение массы бриллиантов')
plt.xlim(0, 3)
plt.axvline(1, color='k', linestyle='--')
plt.xlabel('Масса бриллиант (карат)')
plt.ylabel('Количество бриллиантов (?)')

# упр. добавьте горизонтальную ось с верным названием!

diam2 = diam.assign(ln_price=np.log(diam['price']),
    ln_weight=np.log(diam['carat']))

# две количественных переменных
sns.lmplot(data=diam, x='carat', y='price')

# наблюдений слишком много
sns.jointplot(data=diam, x='carat', y='price', kind='hex')

diam2 = diam.filter(['x', 'y', 'z', 'carat'])
sns.boxplot(data=diam2)


sns.violinplot(data=diam, x='cut', y='price')

# если наблюдений оч мало:
sns.swarmplot(data=diam_small, x='cut', y='price')

corr = diam.corr()
corr
sns.heatmap(corr)
sns.heatmap(corr, annot=True)

sns.catplot(data=diam, col='cut', x='color', y='price',
    kind='violin')
?sns.catplot

grid = sns.FacetGrid(data=diam, col='cut', row='color')
grid.map(plt.hist, 'carat')

sns.pairplot(diam_medium.filter(['x', 'y', 'z', 'color']), hue='color')

sns.lmplot(data=diam_medium, x='carat', y='price', fit_reg=False)

# easy упражнение:
# на diam_medium
# для каждого качества огранки свой график (col)
# # для каждого цвета на графике линия регрессии своего цвета (hue)
sns.lmplot(data=diam_medium, x='carat', y='price', fit_reg=False)

sns.lmplot(data=diam_medium, x='carat', y='price', col='cut',
    hue='color', fit_reg=True)


# квест:
# линия регрессии по всем точкам
# но изобразить случайную выборку из 1000 точек
# seaborn only :)

sns.kdeplot(diam_medium['carat'], diam_medium['price'])
plt.xlim(0, 1.5)
plt.ylim(0, 8000)

