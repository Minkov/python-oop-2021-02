import json
import math
from abc import ABC, abstractmethod


class Shape:
    def perimeter(self):
        pass

    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # def perimeter(self):
    #     return 2 * self.radius * math.pi

    def area(self):
        return self.radius * self.radius * math.pi


print(Circle(10).perimeter())


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __add__(self, other):
        return Square(self.width + other.width)


# csv, xlsx, json

class Serializer(ABC):
    @abstractmethod
    def serialize(self, obj):
        pass


class JsonSerializer(Serializer):
    def serialize(self, obj):
        return json.dumps(obj.__dict__)


class TextSerializer(Serializer):
    def serialize(self, obj):
        return ';'.join(f'{key}={value}' for (key, value) in obj.__dict__.items())


class Serializer2:
    def serialize_json(self, obj):
        return json.dumps(obj.__dict__)

    def serialize_text(self, obj):
        return ';'.join(f'{key}={value}' for (key, value) in obj.__dict__.items())


def get_serializer(type):
    if type == 'json':
        return JsonSerializer()
    else:
        return TextSerializer()


selected_type = 'json'

serializer = get_serializer(selected_type)
print(serializer.serialize(Square(3)))

serializer2 = Serializer2()
if selected_type == 'json':
    print(serializer2.serialize_json(Square(3)))
else:
    print(serializer2.serialize_text(Square(3)))

selected_type = 'text'

serializer = get_serializer(selected_type)
print(serializer.serialize(Square(3)))

if selected_type == 'json':
    print(serializer2.serialize_json(Square(3)))
else:
    print(serializer2.serialize_text(Square(3)))


def print_shape(s: Shape):
    print(f'Inside func with {s}')
    print(f'Perimeter: {s.perimeter()}')
    print(f'Area: {s.area()}')


def print_shapes(shapes: [Shape]):
    for s in shapes:
        print(f'Inside func with {s}')
        print(f'Perimeter: {s.perimeter()}')
        print(f'Area: {s.area()}')


circle = Circle(10)
rect = Rectangle(5, 4)
#
# print_shape(circle)
# print_shape(rect)
# print_shape(1)

print_shapes([
    circle,
    rect,
    Shape(),
    Square(4),
])

# print(dir(Square(3)))

sq1 = Square(3)
sq2 = Square(4)
print(serializer.serialize(sq1 + sq2))
