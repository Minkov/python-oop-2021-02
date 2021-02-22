class Singleton(type):
    __instances = {}

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)
        return cls.__instances[cls]


class PersonFactory(metaclass=Singleton):
    pass


p = PersonFactory()
print(PersonFactory() == PersonFactory())
print(PersonFactory() == PersonFactory())
print(PersonFactory() == PersonFactory())
print(PersonFactory() == PersonFactory())
print(PersonFactory() == PersonFactory())
print(PersonFactory() == PersonFactory())