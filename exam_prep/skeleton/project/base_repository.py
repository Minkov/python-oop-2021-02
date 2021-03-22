from abc import ABC, abstractmethod, abstractproperty


class BaseRepository(ABC):
    def __init__(self):
        self.values = []
        self.identifiers = set()

    @property
    def count(self):
        return len(self.values)

    @abstractmethod
    def get_identifier(self, obj):
        pass

    @abstractmethod
    def get_cannot_add_message(self, obj):
        pass

    @abstractmethod
    def get_cannot_remove_message(self, obj):
        pass

    def add(self, value):
        self.__validate_add_value(value)
        self.values.append(value)
        self.identifiers.add(self.get_identifier(value))

    def remove(self, identifier):
        self.__validate_remove_value(identifier)
        player_index = self.__find_value_index_by_identifier(identifier)
        self.values.pop(player_index)
        self.identifiers.remove(identifier)

    def find(self, identifier):
        return self.values[self.__find_value_index_by_identifier(identifier)]

    def __validate_add_value(self, obj):
        if self.get_identifier(obj) in self.identifiers:
            raise ValueError(self.get_cannot_add_message(obj))

    def __validate_remove_value(self, identifier):
        if not identifier:
            raise ValueError(self.get_cannot_remove_message(identifier))

    def __find_value_index_by_identifier(self, identifier):
        for (index, obj) in enumerate(self.values):
            if self.get_identifier(obj) == identifier:
                return index
