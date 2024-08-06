import numpy as np


def compute_mean(x):
    return np.mean(x)


X = [2, 0, 2, 2, 7, 4, -2, 5, -1, -1]
# print("Mean : ", compute_mean(X))
# Question 1 => A


def compute_median(x):
    X = np.sort(x)
    size = len(X)
    mid = size // 2

    if size % 2 == 0:
        return (X[mid - 1] + X[mid]) / 2
    else:
        return X[mid]


X = [1, 5, 4, 4, 9, 13]
# print("Median: ", compute_median(X))
# Question 2 => B


def compute_std(x):
    mean = np.mean(x)
    variance = np.mean((x - mean) ** 2)
    return np.sqrt(variance)


X = [171, 176, 155, 167, 169, 182]
# print(compute_std(X))
# Question 3 => C


def compute_correlation_cofficient(x, y):
    N = len(x)
    numerator = N * np.sum(x * y) - np.sum(x) * np.sum(y)
    denominator = np.sqrt((N * np.sum(x**2) - np.sum(X)**2)
                          * (N * np.sum(y**2) - np.sum(y)**2))
    return np.round(numerator / denominator, 2)


X = np.asarray([-2, -5, -11, 6, 4, 15, 9])
Y = np.asarray([4, 25, 121, 36, 16, 225, 81])

# print("Correlation: ", compute_correlation_cofficient(X, Y))
# Question 4 => D
