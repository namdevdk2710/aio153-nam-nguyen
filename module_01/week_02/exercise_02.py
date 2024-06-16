'''
Pseudo code
1. Create a function with an argument, a string
2. Create an empty dictionary to store the result
3. Iterate through the string
4. Add the character as a key and the count of the character as a value to the dictionary
5. Return the dictionary

def count_chars(string):
    result = {}
    for char in string:
        result[char] = string.count(char)
    return result
'''


def count_chars(string):
    return {char: string.count(char) for char in string}


print(count_chars('Happiness'))
# {'H': 1, 'a': 1, 'p': 2, 'i': 1, 'n': 1, 'e': 1, 's': 2}
print(count_chars('smiles'))
# {'s': 2, 'm': 1, 'i': 1, 'l': 1, 'e': 1}
print(count_chars('Baby'))
# {'B': 1, 'a': 1, 'b': 1, 'y': 1}
