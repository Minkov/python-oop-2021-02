# class Dog:
#     tricks = []
#
#     def __init__(self, name):
#         self.name = name
#
#     def add_trick(self, trick):
#         self.tricks.append(trick)

class Dog:
    tricks = []

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)


sharo = Dog('Sharo')
puhcho = Dog('Puhcho')

sharo.add_trick('Sit')
puhcho.add_trick('Get the ball')

print(sharo.tricks)
print(puhcho.tricks)
