'''
Pseudo code
1. Create a function that takes two arguments, a list of numbers and an integer k
2. Create an empty list to store the result
3. Iterate through the list of numbers from 0 to len(num_list) - k + 1
4. Append the maximum value of the list of numbers from i to i + k to the result list
5. Return the result list


def max_kernel(num_list, k):
    result = [] 
    for i in range(len(num_list) - k + 1):
        result.append(max(num_list[i:i + k]))
    return result
'''


def max_kernel(num_list, k):
    return [max(num_list[i:i + k]) for i in range(len(num_list) - k + 1)]


print(max_kernel([3, 4, 5, 1, -44, 5, 10, 12, 33, 1], 3))
# [5, 5, 5, 5, 10, 12, 33, 33]
print(max_kernel([3, 4, 5, 1, -44], 3))
# [5, 5, 5]
