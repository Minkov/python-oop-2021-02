class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'{self.name}; {self.age}'


def get_object_by_attr_value(objects, **kwargs):
    result = []
    for obj in objects:
        is_valid = True
        for key, value in kwargs.items():
            if not hasattr(obj, key) or getattr(obj, key) != value:
                is_valid = False
                break

        if is_valid:
            result.append(obj)

    return result


people = [
    Person('Pesho', 11),
    Person('Gosho', 12),
    Person('Pesho', 12),
]

print(get_object_by_attr_value(people, asdasd=None))
