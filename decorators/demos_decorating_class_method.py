import functools


def uppercase(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()

    return wrapper


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @uppercase
    def say_hello(self):
        return f'Hi! I am {self.name}'


print(Person('Gosho', 11).say_hello)
