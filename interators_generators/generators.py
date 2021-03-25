def values_gen(n):
    index = 0
    while index < n:
        yield index
        index += 1


class values_iter:
    def __init__(self, end):
        self.end = end
        # self.index = 0

    def __iter__(self):
        index = 0
        while index < self.end:
            yield index
            index += 1

    # def __next__(self):
    #     index = self.index
    #     self.index += 1
    #     return index


gen = values_gen(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(gen)
for x in gen:
    print(x)

for x in values_iter(5):
    print(f'Gen in iter: {x}')
