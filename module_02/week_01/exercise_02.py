import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

img = mpimg.imread('module_02/week_01/dog.jpeg')


# Question 12 => A
def lightness(vector):
    return np.max(vector) * 0.5 + np.min(vector) * 0.5


question_12 = np.apply_along_axis(lightness, axis=2, arr=img)


# Question 13 => A
def average(vector):
    return np.mean(vector)


question_13 = np.apply_along_axis(average, axis=2, arr=img)


# Question 14 => C
def luminosity(vector):
    return np.dot(vector, [0.21, 0.72, 0.07])


question_14 = np.apply_along_axis(luminosity, axis=2, arr=img)

plt.imshow(question_14, cmap='gray')
plt.show()
