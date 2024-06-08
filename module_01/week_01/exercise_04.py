def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def check_input(x, n):
    if not isinstance(x, (int, float)):
        print("x must be a number")
        return False

    if not isinstance(n, int):
        print("n must be a number")
        return False

    return True


def sin_function(x, n):
    if not check_input(x, n):
        return
    
    result = 0
    for i in range(n + 1):
      sign = (-1) ** i
      term = sign * (x ** (2 * i + 1)) / factorial(2 * i + 1)
      result += term

    print(f"sin({x}) = {result}")


def cos_method(x, n):
    if not check_input(x, n):
        return
    
    result = 0
    for i in range(n + 1):
        sign = (-1) ** i
        term = sign * (x ** (2 * i)) / factorial(2 * i)
        result += term

    print(f"cost({x}) = {result}")


def sinh_method(x, n):
    if not check_input(x, n):
        return
    
    result = 0
    for i in range(n + 1):
        sign = (1) ** i
        term = sign * (x ** (2 * i + 1)) / factorial(2 * i + 1)
        result += term

    print(f"sinh({x}) = {result}")


def cosh_method(x, n):
    if not check_input(x, n):
        return
    
    result = 0
    for i in range(n + 1):
        sign = (1) ** i
        term = sign * (x ** (2 * i)) / factorial(2 * i)
        result += term

    print(f"sinh({x}) = {result}")


sin_function(3.14, 10)
cos_method(3.14, 10)
sinh_method(3.14, 10)
cosh_method(3.14, 10)
