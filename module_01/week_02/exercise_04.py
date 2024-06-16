'''
Pseudo code
1. Create a function with two arguments, source and target
2. If the length of source is less than the length of target, swap the source and target
3. If the length of target is 0, return the length of source
4. Create a list of integers from 0 to the length of target
5. Iterate through the source
6. Create a list of integers with the first element as the index + 1
7. Iterate through the target
8. Calculate the insertions, deletions, and substitutions
9. Append the minimum value of the three to the list
10. Update the previous list with the current list
11. Return the last element of the previous list
'''

def levenshtein_distance(source, target):
    if len(source) < len(target):
        return levenshtein_distance(target, source)

    if len(target) == 0:
        return len(source)

    previous_row = range(len(target) + 1)
    for i, c1 in enumerate(source):
        current_row = [i + 1]
        for j, c2 in enumerate(target):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

print(levenshtein_distance('kitten', 'sitting'))
# 3
print(levenshtein_distance('yu', 'you'))
# 1
print(levenshtein_distance('hi', 'hello'))
# 4
print(levenshtein_distance('halo', 'hello'))
# 2
