ll = [1, 2, 3, 4, 5]

for x in ll:
    print(x)

print([[x + 1] for x in ll])

ll_iter_1 = iter(ll)
ll_iter_2 = iter(ll)
print(ll_iter_1)
# print(f'Iter1: {next(ll_iter_1)}')
# print(f'Iter1: {next(ll_iter_1)}')
# print(f'Iter1: {next(ll_iter_1)}')
# print(f'Iter1: {next(ll_iter_1)}')
# print(f'Iter2: {next(ll_iter_2)}')
#
# print(f'Iter1: {next(ll_iter_1)}')

while True:
    try:
        print(next(ll_iter_1))
    except StopIteration:
        break


