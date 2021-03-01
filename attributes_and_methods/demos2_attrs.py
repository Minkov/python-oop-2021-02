import math
import time


class Person:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

    def __repr__(self):
        return ';'.join(f'{key}={value}' for (key, value) in self.__dict__.items())


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


class Tracker:
    TRACK_ID_KEY = 'track_id'

    def __init__(self):
        self.last_id = 0
        self.objects = []

    def add_object(self, obj):
        self.last_id += 1

        setattr(obj, self.TRACK_ID_KEY, self.last_id)
        self.objects.append(obj)

    def track(self):
        while True:
            for obj in self.objects:
                print(getattr(obj, self.TRACK_ID_KEY, None))
            time.sleep(2)


tracker = Tracker()
pesho = Person('Pesho', 11, 'Burgas', 'Bulgaria')
tracker.add_object(pesho)
tracker.add_object(Circle(4))
print(pesho)
print(Person('Gsoho', 4, 'asd', 'qwe'))

# tracker.track()
