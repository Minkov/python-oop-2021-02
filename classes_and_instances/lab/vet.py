class Vet:
    animals = []
    space = 5

    def __init__(self, name):
        self.name = name
        self.animals = []

    def register_animal(self, animal):
        if Vet.space <= len(Vet.animals):
            return 'Not enough space'

        self.animals.append(animal)
        Vet.animals.append(animal)

        return f'{animal} registered in the clinic'

    def unregister_animal(self, animal):
        if animal not in self.animals:
            return f'{animal} not in the clinic'

        self.animals.remove(animal)
        Vet.animals.remove(animal)

        return f'{animal} unregistered successfully'

    def info(self):
        vet_animals_count = len(self.animals)
        clinic_animals_count = len(Vet.animals)
        space_left = Vet.space - clinic_animals_count
        return f'{self.name} has {vet_animals_count} animals. {space_left} space left in clinic'


peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())
