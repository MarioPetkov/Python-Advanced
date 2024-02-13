class ValueCannotBeNegative(Exception):
    pass

def read_positive_numbers():
    numbers = []
    for i in range(5):
        num = int(input())
        if num < 0:
            raise ValueCannotBeNegative("Negative numbers are not allowed")
        numbers.append(num)
    return numbers

try:
    positive_numbers = read_positive_numbers()
    print("You entered:", positive_numbers)
except ValueCannotBeNegative:
    print("Error:", ValueCannotBeNegative)
