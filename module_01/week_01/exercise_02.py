import math

def is_number(number):
    try:
        float(number)
        return True
    except ValueError:
        return False


def activation_function():
    x = input("Enter x: ")
    if is_number(x) == False:
        print("x must be a number")
        return
    
    method = input("Input activation Function (sigmoid|relu|elu): ")
    if method != 'relu' and method != 'sigmoid' and method != 'elu':
        print(method, " is not supportted")
        return
    
    x = float(x)
    if method == 'relu':
        result = max(0, x)
    elif method == 'sigmoid':
        result = 1 / (1 + math.exp(-x))
    elif method == 'elu':
        result = x if x > 0 else math.exp(x) - 1
    
    print(f"{method}: f({x}) = {result}")


activation_function()
