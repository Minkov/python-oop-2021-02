class Person:
    max_valid_age = 150
    adult_age = 18
    last_id = 0
    name = None
    x = 5

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.id = self.get_id()

    def get_id(self):
        Person.last_id += 1
        return Person.last_id

    # def get_id(self):
    #     print(self.last_id)
    #     # self.last_id += 1
    #     # self.last_id = Person.last_id + 1
    #     print(self.last_id)
    #     return self.last_id

    def say_hello(self):
        print(f'Hello, I am {self.name} and I have id {self.id}')

    def watch_adult_movie(self, movie):
        if self.age < Person.adult_age:
            print('{self.name} are too young')
        else:
            print(f'{self.name} are watching {movie}')

    def check(self):
        print(self == pesho)


def say_hello2(person):
    print(f'Hello, I am {person.name} and I have id {person.id}')


pesho = Person('Pesho', 11)
pesho.say_hello()

say_hello2(pesho)

pesho = Person('Pesho', 11)
gosho = Person('Gosho', 19)

pesho.watch_adult_movie('asd1')
gosho.watch_adult_movie('asd2')  # This way
Person.watch_adult_movie(gosho, 'asd3')  # Not that way

pesho.check()
Person.check(pesho)
# print(pesho.name)
#
# print(Person('Pesho', 11).name)
# print(Person.name)

#
# print(pesho.name)
# pesho.say_hello()
#
# print(Person.max_valid_age)
# print(pesho.max_valid_age)
#
# people = [
#     pesho,
#     Person('Gosho', 3),
# ]
# [p.say_hello() for p in people]
