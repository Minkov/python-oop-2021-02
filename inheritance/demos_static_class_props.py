MIN_AGE = 0
MAX_AGE = 150


class Person:
    min_age = 0
    max_age = 150

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.__age = age  # Don't do this

    # @staticmethod
    # def __validate_age(value):
    #     if value < MIN_AGE \
    #             or MAX_AGE < value:
    #         raise ValueError(f'{value} must be between {MIN_AGE} and {MAX_AGE}')

    @classmethod
    def __validate_age(cls, value):
        if value < cls.min_age \
                or cls.max_age < value:
            raise ValueError(f'{value} must be between {cls.min_age} and {cls.max_age}')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__validate_age(value)
        self.__age = value

    def say_hello(self):
        print(f'Hello, I am {self.name}')

    def __repr__(self):
        return '; '.join(
            f'{key}={value}'
            for (key, value)
            in self.__dict__.items()
        )


#
# MIN_EMPLOYEE_AGE = 16
# MAX_EMPLOYEE_AGE = 150


class Employee(Person):
    min_age = 16

    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    # @staticmethod
    # def __validate_age(value):
    #     if value < MIN_EMPLOYEE_AGE \
    #             or MAX_EMPLOYEE_AGE < value:
    #         raise ValueError(f'{value} must be between {MIN_EMPLOYEE_AGE} and {MAX_EMPLOYEE_AGE}')


gosho = Person('Gosho', -1)
print(gosho)
gosho.age = -2
emp = Employee('Pesho', 17, 1000)
print(Person.min_age)
print(Employee.min_age)
print(emp.age)
print(emp)
