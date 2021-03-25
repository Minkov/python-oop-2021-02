# class custom_range:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#     def __iter__(self):
#         return self.iterator(self)
#
#     def __reversed__(self):
#         return self.iterator(self, is_reversed=True)
#
#     class iterator:
#         def __init__(self, custom_range_obj, is_reversed=False):
#             self.custom_range_obj = custom_range_obj
#             self.is_reversed = is_reversed
#             if is_reversed:
#                 self.value = self.custom_range_obj.end
#             else:
#                 self.value = self.custom_range_obj.start
#
#         def __iter__(self):
#             return self
#
#         def __next__(self):
#             if self.value < self.custom_range_obj.start \
#                     or self.value > self.custom_range_obj.end:
#                 raise StopIteration
#
#             value = self.value
#
#             if self.is_reversed:
#                 self.value -= 1
#             else:
#                 self.value += 1
#             return value

# class reversed_iterator:
#     def __init__(self, custom_range_obj):
#         self.custom_range_obj = custom_range_obj
#         self.value = self.custom_range_obj.end
#
#     def __iter__(self):
#         return self
#
#     def __reversed__(self):
#         return self
#
#     def __next__(self):
#         if self.value < self.custom_range_obj.start:
#             raise StopIteration
#
#         value = self.value
#         self.value -= 1
#         return value

# For judge
class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.value = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.value > self.end:
            raise StopIteration

        value = self.value

        self.value += 1
        return value


cr = custom_range(1, 10)
for x in cr:
    print(f'Iter1: {x}')

for x in cr:
    print(f'Iter2: {x}')

for x in reversed(cr):
    print(f'Reversed: {x}')
