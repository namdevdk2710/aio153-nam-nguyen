import numpy as np


# 1.1 Length of a vector
def compute_vector_length(vector):
    return np.linalg.norm(vector)


# Question 1 => D
vector = np.array([3, 4])
# print(compute_vector_length(vector))


# 1.2 Dot product
def compute_dot_product(vector1, vector2):
    return np.dot(vector1, vector2)


# Question 2 => B
vector1 = np.array([1,2,3])
vector2 = np.array([4,5,6])
# print(compute_dot_product(vector1, vector2))


# 1.3 Multiplying a vector by a matrix
def matrix_multi_vector(matrix, vector):
    return matrix.dot(vector)


# Question 3 => A
# Question 4 => B
# Question 5 => A
matrix = np.array([[-1, 1, 1], [0, -4, 9]])
vector3 = np.array([0, 2, 1])
# print(matrix_multi_vector(matrix, vector3))


# 1.4 Multiplying a matrix by a matrix
def matrix_multi_matrix(matrix1, matrix2):
    return matrix1.dot(matrix2)


# Question 6 => C
# Question 7 => A
# Question 8 => D
# Question 9 => B
matrix1 = np.array([[0, 1, 2], [2, -3, 1]])
matrix2 = np.array([[1, -3], [6, 1], [0, -1]])
# print(matrix_multi_matrix(matrix1, matrix2))


# 1.5 Matrix inverse
def inverse_matrix(matrix):
    return np.linalg.inv(matrix)


# Question 10 => A
matrix3 = np.array([[1,2], [3,4]])
print(inverse_matrix(matrix3))
