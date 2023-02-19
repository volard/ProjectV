import numpy as np
import pandas as pd
import seaborn as sns
import scipy.stats as st
import statsmodels.api as sm
import matplotlib.pyplot as plt
import warnings
from sklearn.preprocessing import StandardScaler

# warnings.filterwarnings('ignore')

datasetPath = 'y_2021_csv.csv'
data = pd.read_csv('y_2021_csv.csv')
data.info()

data.describe()
scaler = StandardScaler()
print(data.head(10))
print(data.isnull().sum())
print(data.describe())
g = sns.pairplot(data, hue='2', plot_kws={"s": 10})
g.fig.set_size_inches(6, 6)
plt.show()

data.corr()
ax = sns.heatmap(data.corr(), annot=True)
plt.show()

print(st.pearsonr(data['1'], data['2']))
print(st.pearsonr(data['1'], data['3']))
print(st.pearsonr(data['2'], data['3']))

print(st.pearsonr(data['1'], data['Result']))
print(st.pearsonr(data['2'], data['Result']))
print(st.pearsonr(data['3'], data['Result']))

pole1 = 'Result'
pole2 = '3'
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
z = np.polyfit(data[pole1], data[pole2], deg=1)
f = np.poly1d(z)
plt.scatter(data[pole1], data[pole2], s=2)
plt.scatter(data[pole1], f(data[pole1]), s=1)
print(f)

residuals = data[pole2] - f(data[pole1])
plt.subplot(1, 2, 2)
plt.scatter(data[pole1], residuals, s=2)
print(np.var(residuals))
plt.show()
plt.subplot(1, 2, 1)
z = np.polyfit(data[pole1], data[pole2], deg=2)
f = np.poly1d(z)
plt.scatter(data[pole1], data[pole2], s=2)
plt.scatter(data[pole1], f(data[pole1]), s=1)
print(f)

residuals = data[pole2] - f(data[pole1])
plt.subplot(1, 2, 2)
plt.scatter(data[pole1], residuals, s=2)
print(np.var(residuals))
plt.show()

corrCoeff = np.corrcoef(data[pole1], data[pole2])[0][1]


def index_cor():
    n = len(data[pole2].index)
    sum_sq = np.sum(data[pole2] ** 2)
    sum_y_sq = np.sum(f(data[pole1]) ** 2)
    local_sum = np.sum(data[pole2])
    return ((n * sum_y_sq - local_sum ** 2) / (n * sum_sq - local_sum ** 2)) ** (1 / 2)


plt.plot(data[pole1].sort_values(), f(data[pole1].sort_values()))
plt.scatter(data[pole1], data[pole2], color="orange")

print('Индекс корреляции: ', round(index_cor(), 3))
print('Коэффициент корреляции Пирсона: ', round(corrCoeff, 2))

y = data['1'].values
x = data[[pole1, pole2]].values.T

y1 = data['2'].values
x1 = data[[pole1, pole2]].values.T

y2 = data['3'].values
x2 = data[[pole2]].values.T


def reg_m(_y, _x):
    ones = np.ones(len(_x[0]))
    X = sm.add_constant(np.column_stack((_x[0], _x[1], ones)))
    results = sm.OLS(_y, X).fit()
    return results


# print(reg_m(y, x).summary())
# print(reg_m(y1, x1).summary())
# print(reg_m(y2, x2).summary())
#
# reg_m(y1, x1)
# plt.show()

