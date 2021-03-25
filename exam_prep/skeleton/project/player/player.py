from abc import ABC, abstractmethod

from project.card.card_repository import CardRepository


class Player(ABC):
    def __init__(self, username, health):
        self.username = username
        self.health = health
        self.card_repository = CardRepository()

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.validate_username(value)
        self.__username = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.validate_health(value)
        self.__health = value

    @property
    def is_dead(self):
        return self.health <= 0

    @property
    def damage(self):
        return sum(card.damage_points for card in self.card_repository.cards)

    @abstractmethod
    def apply_bonuses(self):
        pass

    def take_damage(self, damage_points):
        if damage_points < 0:
            raise ValueError('Damage points cannot be less than zero.')

        self.health -= damage_points

    @staticmethod
    def validate_username(value):
        if not value:
            raise ValueError('Player\'s username cannot be an empty string. ')

    @staticmethod
    def validate_health(value):
        if value < 0:
            raise ValueError('Player\'s health bonus cannot be less than zero')
