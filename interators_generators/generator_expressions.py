from math import sqrt


def is_prime(number):
    for x in range(2, int(sqrt(number)) + 1):
        if number % x == 0:
            return False

    return True


def primes(max_number):
    return (x for x in range(max_number) if is_prime(x))


ll = [x for x in range(5)]
print(ll)

print(list(primes(50)))
print(list(primes(50)))
