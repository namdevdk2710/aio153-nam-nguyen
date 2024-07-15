import numpy as np

# Question 1 => A
question_1 = np.arange(0, 10, 1)
# print(question_1)


# Question 2 => D
question_2 = np.ones((3, 3)) > 0
question_2 = np.ones((3, 3), dtype=bool)
question_2 = np.full((3, 3), fill_value=True, dtype=bool)
# print(question_2)


# Question 3 => A
question_3 = np.arange(0, 10)
# print(question_3[question_3 % 2 == 1])


# Question 4 => B
question_4 = np.arange(0, 10)
question_4[question_4 % 2 == 1] = -1
# print(question_4)


# Question 5 => B
question_5 = np.arange(10)
question_5_2d = question_5.reshape(2, -1)
# print(question_5_2d)

# Question 6 => A
question_6_1 = np.arange(10).reshape(2, -1)
question_6_2 = np.repeat(1, 10).reshape(2, -1)
question_6 = np.concatenate([question_6_1, question_6_2], axis=0)
# print(question_6)


# Question 7 => C
question_7_1 = np.arange(10).reshape(2, -1)
question_7_2 = np.repeat(1, 10).reshape(2, -1)
question_7 = np.concatenate([question_7_1, question_7_2], axis=1)
# print(question_7)


# Question 8 => A
question_8 = np.array([1, 2, 3])
# print(np.repeat(question_8, 3))
# print(np.tile(question_8, 3))


# Question 9 => C
question_9 = np.array([2, 6, 1, 9, 10, 3, 27])
index = np.where((question_9 >= 5) & (question_9 <= 10))
# print(question_9[index])


# Question 10 => D
def find_max(x, y):
    if x >= y:
        return x
    else:
        return y


question_10_a = np.array([5, 7, 9, 8, 6, 4, 5])
question_10_b = np.array([6, 3, 4, 8, 9, 7, 1])
pair_max = np.vectorize(find_max, otypes=[float])
# print(pair_max(question_10_a, question_10_b))


# Question 11 => Ket qua sai => [6 7 9 8 9 7 5] => C
question_11_a = np.array([5, 7, 9, 8, 6, 4, 5])
question_11_b = np.array([6, 3, 4, 8, 9, 7, 1])
print(np.where(question_11_a < question_11_b,
               question_11_b, question_11_a))
