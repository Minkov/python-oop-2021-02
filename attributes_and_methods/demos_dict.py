class Person:
    def __init__(self, name):
        self.name = name

    def get_attributes_with_prefix(self, prefix):
        return [key for (key) in self.__dict__.keys() if key.startswith(prefix)]

    def set_later_value(self):
        self.age = 17

    def set_dict_value(self):
        self.__dict__['something'] = 5

    def __repr__(self):
        return ';'.join(f'{key}={value}' for (key, value) in self.__dict__.items())


pesho = Person('Pesho')
print(pesho.__dict__)
print(pesho)
pesho.set_later_value()
print(pesho.__dict__)
print(pesho)

del pesho.age
print(pesho.__dict__)
print(pesho)

print(pesho.get_attributes_with_prefix('name'))

pesho.name_lower = 'pesho'
print(pesho.get_attributes_with_prefix('name'))

print(pesho)
pesho.set_dict_value()
print(pesho)
