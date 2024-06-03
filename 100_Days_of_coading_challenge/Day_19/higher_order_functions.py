# HIGHER ORDER FUNCTIONS :a function that can work with other functions, at that time the function
# that is within the other function does not need a parenthesis

# calculate function is the HIGHER ORDER FUNCTION.
def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


def calculate(n1, n2, func):
    return func(n1, n2)


result = calculate(2, 3, mul)
print(result)
