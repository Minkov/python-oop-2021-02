from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print('Drawing circle')


class Rectangle(Shape):
    def draw(self):
        print('Drawing rect')


Circle().draw()
Rectangle().draw()
