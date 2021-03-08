import random


class RandomList(list):
    def get_random_element(self):
        element_index = random.randint(0, len(self) - 1)
        element = self[element_index]
        self.pop(element_index)
        return element

class RandomList2(list):
    def get_random_element(self):
        el = random.choice(self)
        self.remove(el)
        return el

rl = RandomList([1, 2, 1, 3, 4, 5])
while rl:
    print(rl.get_random_element())
