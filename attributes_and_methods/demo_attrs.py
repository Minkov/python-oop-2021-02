import math


class Person:
    max_age = 150

    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

    def something(self):
        pass

    def __repr__(self):
        return ';'.join(f'{key}={value}' for (key, value) in self.__dict__.items())


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


def get_values(obj, attr_names):
    return [getattr(obj, attr_name, None) for attr_name in attr_names]
    # result = []
    # for attr_name in attr_names:
    #     if attr_name == 'name':
    #         result.append(obj.name)
    #     elif attr_name == 'age':
    #         result.append(obj.age)
    #     elif attr_name == 'city':
    #         result.append(obj.city)
    #     elif attr_name == 'country':
    #         result.append(obj.country)
    #     else:
    #         result.append(None)
    # return result


pesho = Person('Pesho', 11, 'Sofia', 'Bulgaria')

print(getattr(pesho, 'name'))
print(pesho.name)
print(get_values(pesho, ['city', 'country']))  # [Sofia, Bulgaria]
print(get_values(pesho, ['name', 'country']))  # [Pesho, Bulgaria]
print(get_values(pesho, ['name', 'middle_name']))  # [Pesho, Bulgaria]

circle = Circle(4)
print(get_values(circle, ['radius']))
print(get_values(circle, ['radius', 'area']))
area_method = get_values(circle, ['area'])[0]
print(area_method)
print(area_method())

print(getattr(circle, 'radius', None))
print(getattr(circle, 'diameter', None))

print(hasattr(circle, 'radius'))
print(hasattr(circle, 'diameter'))

print(getattr(circle, 'radius', None))
print(getattr(circle, 'radius') if hasattr(circle, 'radius') else None)

print(getattr(circle, 'diameter', None))
print(getattr(circle, 'diameter') if hasattr(circle, 'diameter') else None)

print(pesho)

pesho.city = 'Burgas'
print(pesho)

setattr(pesho, 'city', 'Varna')
print(pesho)

setattr(pesho, 'middle', 'Georgiev')
print(pesho)

delattr(pesho, 'middle')
print(pesho)


# delattr(pesho, 'middle')

def print_name():
    print('It works')


setattr(pesho, 'print_name', print_name)
pesho.print_name()

print(getattr(Person, 'something'))
print(getattr(Person, 'max_age'))
