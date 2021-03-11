import json
import math

from abc import ABC, abstractmethod


class Serializer(ABC):
    def __init__(self, print_func):
        self.print_func = print_func

    @abstractmethod
    def serialize(self, obj):
        pass

    def print(self, obj):
        self.print_func(self.serialize(obj))


class JsonSerializer(Serializer):
    def serialize(self, obj):
        return json.dumps(obj.__dict__)


class Shape:
    def __init__(self):
        if type(self) == Shape:
            raise TypeError('Shape is abstract')

    def area(self):
        raise TypeError('area() is abstract')


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


# print(Circle(10))
# print(Circle(10).area())
JsonSerializer(print) \
    .print(Circle(10))
