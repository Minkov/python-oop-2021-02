from abc import ABC, abstractmethod


class ValidatorBase(ABC):
    @abstractmethod
    def validate(self, *args, **kwargs):
        pass


class TypeValidator(ValidatorBase):
    def validate(self, value, types):
        if type(value) not in types:
            raise ValueError('`numbers` should be numbers')
