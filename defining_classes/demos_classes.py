def init(person, name, age):
    person.name = name
    person.age = age


class Person:
    min_age = 0
    max_age = 150

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_older(self):
        self.age += 1

    def get_info(self):
        return f'{self.name}; {self.age}'

    # __call__, __new__
    def __str__(self):
        return self.get_info()

    def __add__(self, other):
        return Person(self.name + other.name, self.age + other.age)


print(Person.get_info)
print(Person.min_age, Person.max_age)
#
pesho = Person('Pesho', 15)
print(pesho.get_info())
print(Person.get_info(pesho))

# stamo = Person('Stamo', 11)
# print(pesho)
# print(stamo)
# pesho.get_older()
# print(pesho)
# print(stamo)
#
# print(pesho + stamo)
#
# str()
