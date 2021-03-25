from math import sqrt


def is_prime(number):
    for x in range(2, int(sqrt(number)) + 1):
        if number % x == 0:
            return False

    return True


#     1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
#     T T T T T T T T T  T  T  T  T  T  T  T  T  T
# (2)        F   F   F    F     F     F     F     F
# (3)            F     F        F        F        F
#     T T T F T F T F F  F  T  F  T  F  F  F  T  F
#     1 2 3   5   7        11    13          17
def primes_gen(max_number):
    number = 1
    while number < max_number:
        if is_prime(number):
            yield number
        number += 1


class Primes:
    def __init__(self, max_number):
        self.max_number = max_number
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.number > self.max_number:
            raise StopIteration
        number = self.number
        self.number += 1
        if not is_prime(number):
            return self.__next__()
        return number


print(list(primes_gen(50)))
print(list(Primes(50)))
