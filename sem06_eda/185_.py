# To add a new cell, type '#'
# To add a new markdown cell, type '# [markdown]'
#
import numpy as np


#
matrix = [[1,2,3], [4,5,6],[8,7,9]]
matrix = np.array(matrix)
matrix


#
type(matrix)


#
matrix.ndim


#
np.linalg.eigvals(matrix)


#
np.linalg.eig(matrix)


#
np.eye(4)


#
np.zeros((3,3,3))


#
X = np.random.normal(loc=5, scale=3, size=(4,5))
X

# [markdown]
# **Задание:**
# 
# Элемент из X, который ближе всего к v по абсолютной величине. 

#
def nearest_value(X, v):
    Y = np.abs(X - v)
    mn = np.min(Y)
    return X[np.where(Y == mn)][0]


#
v = 3.6
nearest_value(X, v)

# [markdown]
# **Задание:** 
# 
# Реализовать подсчёт произведения всех элементов по диагонали

#
X = np.random.normal(loc=5, scale=3, size=(5,5))

def diag_prod(X):
    return np.prod(np.diag(X))

diag_prod(X)

# [markdown]
# **Задание:** 
# 
# 

#
X = np.random.random((2,3))*100
Y = np.random.chisquare(df=5, size=(2,3))*10

X


#
Y

# [markdown]
# $$
# \cos(x,y) = \frac{(x,y)}{||x|| \cdot ||y|| }
# $$
# 
# $$
# (x,y) = \sum_i x_i \cdot y_i
# $$
# 
# $$
# ||x|| = \sqrt{(x,x)} = \sqrt{\sum_i x_i^2}
# $$

#
x = X[0]
y = Y[0]
x, y


#
X.shape


#
Z = X[:, np.newaxis] * Y
Z.shape


#
Z


#
Z


#
np.sqrt(np.sum(X**2, axis=1))[:,np.newaxis]*np.sqrt(np.sum(Y**2, axis=1))


#
Z1 = (X[:, np.newaxis] * Y).sum(axis=2)
Z2 = np.sqrt(np.sum(X**2, axis=1))[:,np.newaxis]*np.sqrt(np.sum(Y**2, axis=1))

Z1/Z2


#
# проверка 
x = X[1]
y = Y[1]

np.sum(x*y)/(np.sqrt(np.sum(x**2))*np.sqrt(np.sum(y**2)))


#
pwd


#
import pandas as pd

path = "/Users/randomwalk/Desktop/data/data_football_profile.csv"

df = pd.read_csv(path, sep="\t")
df.head( )


#
df.shape


#
df["Wage"].mean()


#
df.isnull().sum()


#
import seaborn as sns
import matplotlib.pyplot as plt 

plt.figure(figsize=(15,10))
sns.heatmap(df.isnull())


#
df.shape


#
df.dropna( ).shape


#
df.drop("Value", axis=1, inplace=True)
# либо
# df = df.drop("Value", axis=1)
df.head()


#
df.shape


#
df.dropna(inplace=True)
df.shape


#
df["Club"].unique().size


#
df["Club"].value_counts().hist()


#
(df["Age"] == 31).sum()


#
df[df["Age"] == 31]["Wage"].mean()


#
df[df["Age"] == 29]["Wage"].mean()

# [markdown]
# $$
# \bar x \pm z_{1 - \frac{\alpha}{2}} \cdot \sqrt{\frac{\sigma^2}{n}}
# $$

#
df_agg = df.groupby("Age")["Wage"].agg(["mean", "count", "std"])
df_agg["left"] = df_agg["mean"] - 1.96*df_agg["mean"]/np.sqrt(df_agg["mean"])
df_agg["right"] = df_agg["mean"] + 1.96*df_agg["mean"]/np.sqrt(df_agg["mean"])


#
df_agg[["left", "right", "mean"]].plot(figsize = (15,7));


#



#



#


