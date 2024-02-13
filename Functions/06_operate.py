from functools import reduce

def operate(operator, *args: int):
    if operator == '+':
        return reduce(lambda x, y: x + y, args)
    if operator == '-':
        return reduce(lambda x, y: x - y, args)
    if operator == '*':
        return reduce(lambda x, y: x * y, args)
    if operator == '/':
        return reduce(lambda x, y: x / y, args)



print(operate("+", 1, 2, 3))