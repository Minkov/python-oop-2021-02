from app.validators import TypeValidator


class Utils:
    def __init__(self):
        self.validator = TypeValidator()

    def sum(self, numbers):
        [self.validator.validate(x, [int, float]) for x in numbers]
        return sum(numbers)
