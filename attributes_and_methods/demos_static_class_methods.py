def is_age_valid(age):
    return 0 <= age <= Person.max_age


class Person:
    max_age = 150

    def __init__(self, name, age):
        self.validate_age(age)
        self.name = name
        self.age = age

    @staticmethod
    def validate_age(age):
        if age < 0 or Person.max_age < age:
            raise ValueError('Age is invalid')

    @staticmethod
    def is_age_valid(age):
        return 0 <= age <= Person.max_age

    @staticmethod
    def nestho_si():
        return 'neshto si'

    @classmethod
    def is_age_valid(cls, age):
        if not hasattr(cls, 'max_age'):
            raise TypeError(f'{cls} must have class attribute `max_age`')
        return 0 <= age <= cls.max_age


# print(Person('Gosho', 11))
# print(Person.is_age_valid(5))
# print(Person.is_age_valid(555))
#
# print(Person.nestho_si())
#
# print(Person('Gosho', 1111))

# print(Person.is_age_valid(5))
# print(Person.is_age_valid(555))

# class Circle:
#     def __init__(self, radius=None, diameter=None):
#         self.radius = radius if radius else diameter / 2
#
#     def __repr__(self):
#         return f'radius: ${self.radius}'

#
# diameter = 10
#
# circle = Circle(diameter=diameter)

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __repr__(self):
        return str(self.__dict__)

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return str(self.__dict__)

    @classmethod
    def with_equal_sides(cls, side):
        return cls(side, side)

    # don't do this. Use classmethod
    @staticmethod
    def with_equal_sides2(cls, side):
        return cls(side, side)


print(Circle(5))
print(Circle.from_diameter(10))
print(Rectangle(5, 10))
print(Rectangle.with_equal_sides(3))
print(Rectangle.with_equal_sides2(Rectangle, 3))
