from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def un_execute(self):
        pass


class AddCommand(Command):
    def __init__(self, values, new_value):
        self.values = values
        self.new_value = new_value

    def execute(self):
        self.values.append(self.new_value)

    def un_execute(self):
        self.values.pop()


class SumCommand(Command):
    def __init__(self, values):
        self.values = values

    def execute(self):
        return sum(self.values)

    def un_execute(self):
        return sum(self.values)


class RemoveLastCommand(Command):
    def __init__(self, values):
        self.values = values
        self.removed_value = None

    def execute(self):
        self.removed_value = self.values.pop()

    def un_execute(self):
        self.values.append(self.removed_value)
        self.removed_value = None


class RemoveFirstCommand(Command):
    def __init__(self, values):
        self.values = values
        self.removed_value = None

    def execute(self):
        self.removed_value = self.values.pop(0)

    def un_execute(self):
        self.values.insert(0, self.removed_value)
        self.removed_value = None


class CommandsMemento:
    def __init__(self, values):
        self.state = list(values)


commands = []
values = []

while True:
    command_text = input()
    if command_text == 'END':
        break

    if command_text == 'REMOVE_LAST':
        command = RemoveLastCommand(values)
    elif command_text == 'REMOVE_FIRST':
        command = RemoveFirstCommand(values)
    elif command_text == 'SUM':
        command = SumCommand(values)
    else:
        _, value = command_text.split(' ')
        command = AddCommand(values, int(value))

    commands.append(command)

mementos = []

for command in commands:
    print(command.execute())

for memento in mementos:
    print(memento.state)

print('----')

print(values)
for command in commands[::-1]:
    print(command.un_execute())

print(values)
"""
ADD 5
ADD 6
SUM
REMOVE_FIRST
ADD 3
ADD 7
SUM
REMOVE_LAST
SUM
REMOVE_LAST
SUM
REMOVE_LAST
SUM
END
"""
