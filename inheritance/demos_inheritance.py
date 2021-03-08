class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f'Hello, I am {self.name}')


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        # super(Employee, self).__init__(name) # old school
        # Person.__init__(self, name, age)
        self.salary = salary

    # overwriting
    def say_hello(self):
        # super().say_hello()
        print(f'My name is {self.name} and my salary is {self.salary}')


emp = Employee('Pesho', 11, 1000)
emp.say_hello()
