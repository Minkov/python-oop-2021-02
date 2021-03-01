class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        result = 1
        for arg in args:
            result *= arg
        return result

    @staticmethod
    def divide(initial, *args):
        result = initial
        for arg in args:
            result /= arg
        return result

    @staticmethod
    def subtract(initial, *args):
        result = initial
        for arg in args:
            result -= arg
        return result


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
