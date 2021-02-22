class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def get_free_size(self):
        return self.size - self.quantity

    def fill(self, milliliters):
        if self.get_free_size() < milliliters:
            return

        self.quantity += milliliters

    def status(self):
        return self.get_free_size()


cup = Cup(100, 50)
cup.fill(50)
cup.fill(10)

print(cup.status())
