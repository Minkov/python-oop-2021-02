class DefaultReprMixin:
    def __repr__(self):
        return '; '.join(
            f'{key}={value}'
            for (key, value)
            in self.__dict__.items()
        )


class Person(DefaultReprMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary


class Formatter(DefaultReprMixin):
    def __init__(self, format):
        self.format = format


print(Formatter.mro())
print(Person('Gosho', 11))
print(Formatter('xml'))
print(Employee('xml', 12, 100))
