from project.animal import Animal
from project.cat import Cat
from project.dog import Dog

animal = Animal()
print(animal.eat())

dog = Dog()
print(dog.bark())
print(dog.eat())

cat = Cat()
print(cat.meow())
print(cat.eat())