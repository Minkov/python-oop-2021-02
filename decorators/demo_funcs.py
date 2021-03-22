def operation(type):
    def sum_two(x, y):
        return x + y

    def multiply_two(x, y):
        return x * y

    if type == '+':
        return sum_two
    elif type == '*':
        return multiply_two
    else:
        raise ValueError('Supported operations are \'+\' and \'*\'')


# sum_operation = operation('+')
# print(sum_operation)
# print(sum_operation(1, 2))

def calculator():
    # result = [0]
    result = 0

    def add(x):
        nonlocal result
        result += x
        # result[0] += x

    def multyply(x):
        nonlocal result
        result *= x
        # result[0] *= x

    def get_result():
        return result
        # return result[0]

    return (add, multyply, get_result)


(add1, multiply1, get_result1) = calculator()
(add2, multiply2, get_result2) = calculator()

print(get_result1())
add1(3)
print(get_result1())
add1(2)
print(get_result1())
multiply1(2.5)
print(get_result1())

print(get_result2())
