import pandas as pd
import numpy as np


def compute_cosine(vector1, vector2):
    return np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))


# Question 12 => C
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])
print(compute_cosine(vector1, vector2))
