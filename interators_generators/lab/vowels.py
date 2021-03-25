# Iterator
# class vowels:
#     vowels = {
#         'a', 'e', 'y', 'u', 'o', 'i',
#         'A', 'E', 'Y', 'U', 'O', 'I',
#     }
#
#     def __init__(self, text):
#         self.text = text
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= len(self.text):
#             raise StopIteration
#         ch = self.text[self.index]
#         self.index += 1
#         if ch not in self.vowels:
#             return self.__next__()
#
#         return ch

# Generator function
# def vowels(text):
#     vowels = {
#         'a', 'e', 'y', 'u', 'o', 'i',
#         'A', 'E', 'Y', 'U', 'O', 'I',
#     }
#
#     for ch in text:
#         if ch in vowels:
#             yield ch

# generator comprehension
def vowels(text):
    vowels = {
        'a', 'e', 'y', 'u', 'o', 'i',
        'A', 'E', 'Y', 'U', 'O', 'I',
    }

    return (ch for ch in text if ch in vowels)


my_string = vowels('AbcvasElppIplleliyttlYtortOsdUwu')
for char in my_string:
    print(char)
