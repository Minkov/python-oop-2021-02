# x = 5
#
#
# def print_x():
#     print(f'Print {x}')
#
#
# print(x)
# print_x()
#
#
# def f1():
#     def nested_f1():
#         # nonlocal y
#         # y += 1
#         y = 88
#         ll.append(3)
#         # ll = [3]
#         z = 7
#         print('From nested f1')
#         print(x)
#         print(y)
#         print(z)
#         print(abs(-x - y - z))
#
#     global name
#     name = 'Pesho'
#     global x
#     x += 5
#     y = 6
#     ll = []
#     print(f'Before: {y}')
#     print(ll)
#     nested_f1()
#     print(ll)
#     print(f'After: {y}')
#     return 'Pesho'
#
#
# f1()
# print(name)
# # print(y)

def get_my_print():
    count = 0

    def my_print(x):
        nonlocal count
        count += 1
        print(f'My ({count}): {x}')

    return my_print


my_print = get_my_print()
my_print('1')
my_print('Pesho')
my_print('Apples')
