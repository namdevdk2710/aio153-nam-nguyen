import pandas as pd
import numpy as np

df = pd.read_csv('module_02/week_01/advertising.csv')

sales_data = df['Sales']
tv_data = df['TV']
newspaper_data = df['Newspaper']

average_sales = np.mean(sales_data)


# Question 15 => C
question_15_max = np.max(sales_data)
question_15_index = np.argmax(sales_data)
# print(question_15_max, question_15_index)


# Question 16 => B
question_16 = np.mean(tv_data)
# print(question_16)


# Question 17 => A
question_17 = np.sum(sales_data >= 20)
# print(question_17)


# Question 18 => B
question_18 = np.mean(df[sales_data >= 15]['Radio'])
# print(question_18)


# Question 19 => C
average_newspaper = np.mean(newspaper_data)
question_19 = np.sum(df[newspaper_data > average_newspaper]['Sales'])
# print(question_19)


# Question 20 => C
question_20 = np.where(sales_data > average_sales, 'Good', np.where(
    sales_data == average_sales, 'Average', 'Bad'))
# print(question_20[7:10])


# Question 21 => C
closest_average_sales = sales_data[np.argmin(abs(sales_data - average_sales))]
question_21 = np.where(sales_data > closest_average_sales, 'Good', np.where(
    sales_data < closest_average_sales, 'Bad', 'Average'))
# print(question_21[7:10])
