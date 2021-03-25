# class reverse_iter:
#     def __init__(self, iterable):
#         self.iterable = iterable
#
#     def __iter__(self):
#         return self.iterator(self)
#
#     class iterator:
#         def __init__(self, reverse_iter_obj):
#             self.list = list(reverse_iter_obj.iterable)
#             self.index = len(self.list) - 1
#
#         def __iter__(self):
#             return self
#
#         def __next__(self):
#             if self.index < 0:
#                 raise StopIteration
#             value = self.list[self.index]
#             self.index -= 1
#             return value

class reverse_iter:
    def __init__(self, iterable):
        self.list = list(iterable)
        self.index = len(self.list) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.list[self.index]
        self.index -= 1
        return value


ri = reverse_iter([1, 2, 3])

for x in ri:
    print(x)

for x in ri:
    print(x)
