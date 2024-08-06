import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("module_02/week_04/advertising.csv")


def correlation(x, y):
    N = len(x)
    numerator = N * np.sum(x * y) - np.sum(x) * np.sum(y)
    denominator = np.sqrt((N * np.sum(x**2) - np.sum(x)**2)
                          * (N * np.sum(y**2) - np.sum(y)**2))
    return numerator / denominator


x = data['TV']
y = data['Radio']
corr_xy = correlation(x, y)

# print(f"Correlation between TV and Radio: {round(corr_xy, 2)}")
# Question 5 => B


features = ['TV', 'Radio', 'Newspaper']
for feature_1 in features:
    for feature_2 in features:
        correlation_value = correlation(data[feature_1], data[feature_2])
        # print(f"{feature_1} and {feature_2}: {round(correlation_value, 2)}")

# Question 6 => D


x = data['Radio']
y = data['Newspaper']

result = np.corrcoef(x, y)
# print(result)
# Question 7 => C


result = data.corr()
# print(result)
# Question 8 => D


plt.figure(figsize=(10, 8))
sns.heatmap(result, annot=True, fmt=".2f", linewidths=.5)
plt.show()
# Question 9 => B
