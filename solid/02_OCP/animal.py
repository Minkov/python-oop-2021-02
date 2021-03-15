from abc import ABC, abstractmethod


class Animal:
    # Wrong on so many levels:
    # Violation of Liskov Substitute Principle
    # No abstraction
    # No polymorphism here
    def eat(self):
        if type(self) in [Dragon, Dog, Cat]:
            print('I eat meat')
        elif type(self) in [Mole, Bird]:
            print('I eat grass')


class FlyingMixin:
    def fly(self):
        pass


class SoundMakingAnimal(Animal, ABC):
    @abstractmethod
    def get_sound(self):
        pass


class NotSoundMakingAnimal(Animal, ABC):
    pass


class Mole(Animal):
    # Example of violation
    def get_sound(self):
        raise TypeError('Moles cannot make sound')


class Bird(NotSoundMakingAnimal, FlyingMixin):
    pass


class Cat(SoundMakingAnimal):
    sound = 'meow'

    def get_sound(self):
        return self.sound


class Dog(SoundMakingAnimal):
    sound = 'woof-woof'

    def get_sound(self):
        return self.sound


class Dragon(SoundMakingAnimal, FlyingMixin):
    sound = 'rawr'

    def get_sound(self):
        return self.sound


class Donkey(SoundMakingAnimal):
    sound = 'I am a talinkg donkey'

    def get_sound(self):
        return self.sound


def animal_sound(animals: list[SoundMakingAnimal]):
    for animal in animals:
        print(animal.get_sound())


def animal_eat(animals: list[Animal]):
    for animal in animals:
        print(animal.eat())
        if type(animal) != Dragon:
            pass


animals = [Cat(), Dog(), Dragon(), Donkey()]
animal_sound(animals)
animal_eat(animals + [Mole()])
