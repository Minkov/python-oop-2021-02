class Person:
    MIN_AGE = 0
    MAX_AGE = 150

    def __init__(self, first_name, last_name, age, city=None):
        self.first_name = first_name
        self.last_name = last_name
        # self.__age = age
        self.set_age(age)
        self.city = city

    @staticmethod
    def __validate_name(name):
        if not name:
            raise ValueError('Name cannot be None')

    # Invalid
    @staticmethod
    @property
    def static_prop():
        print('Static property')
        return 'Static property'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    # getter
    @property
    def first_name(self):
        return self.__first_name

    # setter
    @first_name.setter
    def first_name(self, new_name):
        self.__validate_name(new_name)
        self.__first_name = new_name

    # Dont do this
    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, new_city):
        self.__city = new_city
        # self.city = new_city

    def set_age(self, new_age):
        if new_age < Person.MIN_AGE or Person.MAX_AGE < new_age:
            raise ValueError(f'Age must be between {Person.MIN_AGE} and {Person.MAX_AGE}')
        self.__age = new_age

    def get_age(self):
        return self.__age

    # def __setattr__(self, key, value):
    #     if len(key) > 1 and key.startswith('_') and key[1] != '_':
    #         key = f'_{self.__class__.__name__}${key}'
    #
    #     return super().__setattr__(key, value)
    #
    # def __getattr__(self, item):
    #     if len(item) > 1 and item.startswith('_') and item[1] != '_':
    #         item = f'_{self.__class__.__name__}${item}'
    #     return super().__getattribute__(item)


print(Person.static_prop)
pesho = Person('Pesho', 'Georgiev', 11)
print(pesho.__first_name)
print(pesho.__dict__)
print(pesho.get_age())
print(pesho.full_name)
pesho.full_name = 'Georgi Georgiev'

# print(pesho._Person$age)
# print(pesho.__age)

# pesho.__age = -1
# pesho.set_age(-1)
# print(pesho.__dict__)
# print(pesho.get_age())

print(Person._Person__validate_name)
print(pesho._Person__validate_name)

pesho.first_name = None
print(pesho.__dict__)
print(pesho.first_name)
