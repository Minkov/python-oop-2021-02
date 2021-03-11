# import json
# import math
#
#
# class Shape:
#     def perimeter(self):
#         pass
#
#     def area(self):
#         pass
#
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def perimeter(self):
#         return 2 * self.radius * math.pi
#
#     def area(self):
#         return self.radius * self.radius * math.pi
#
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
#     def area(self):
#         return self.width * self.height
#
#
# class Square(Rectangle):
#     def __init__(self, side):
#         super().__init__(side, side)
#
#
# class JsonSerializer:
#     def serialize(self, obj):
#         return json.dumps(obj.__dict__)
#
#
# class TextSerializer:
#     def serialize(self, obj):
#         return ';'.join(f'{key}={value}' for (key, value) in obj.__dict__.items())
#
#
# def get_serializer(type):
#     if type == 'json':
#         return JsonSerializer()
#     else:
#         return TextSerializer()
#
#
# selected_type = 'json'
#
# serializer = get_serializer(selected_type)
# print(serializer.serialize(Square(3)))


class Dog:
    def sound(self):
        print('Djaf')


class Car:
    def sound(self):
        print('Brum brum')


def make_sound(obj):
    obj.sound()


make_sound(Dog())

make_sound(Car())
