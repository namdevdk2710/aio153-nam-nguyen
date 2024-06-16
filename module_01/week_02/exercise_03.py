'''
Pseudo code
1. Create a function with an argument, a path to a file
2. Open the file
3. Read the content of the file
4. Standardlize and sort the content
5. Close the file
6. Create an empty dictionary to store the result
7. Iterate through the content
8. Add the word as a key and the count of the word as a value to the dictionary
9. Return the dictionary

def word_count(file_path):
    file = open(file_path, 'r')
    data = sorted(standardlize(file.read()))
    file.close()
    result = {}
    for word in data:
        result[word] = data.count(word)
    return result
'''


def standardlize(data: str):
    return data.lower().replace('\n', '').replace(',', '').split(' ')


def word_count(file_path):
    file = open(file_path, 'r')
    data = sorted(standardlize(file.read()))
    file.close()

    return {word: data.count(word) for word in data}


print(word_count('./module_01/week_02/P1_data.txt'))
