from abc import ABC, abstractmethod


class SoundMaker:
    def make_sound(self, sound):
        return sound


class Flyer:
    def fly(self):
        pass


class Eater:
    def eat(self):
        pass


class Animal:
    def __init__(self, eater):
        self.eater = eater

    def eat(self):
        return self.eater.eat()


class SoundMakingAnimal(Animal, ABC):
    def __init__(self, eater, sound_maker, sound):
        super().__init__(eater)
        self.sound_maker = sound_maker
        self.sound = sound

    def get_sound(self):
        return self.sound_maker.make_sound(self.sound)


def animal_sound(animals: list[SoundMakingAnimal]):
    for animal in animals:
        print(animal.get_sound())


def animal_eat(animals: list[Animal]):
    for animal in animals:
        print(animal.eat())


eater = Eater()
sound_maker = SoundMaker()
animals = [
    SoundMakingAnimal(eater, sound_maker, 'meow'),
    SoundMakingAnimal(eater, sound_maker, 'woof-woof'),
    SoundMakingAnimal(eater, sound_maker, 'rawr'),
    SoundMakingAnimal(eater, sound_maker, 'I am a talking donkey')
]
animal_sound(animals)
animal_eat(animals + [Animal(Eater())])
