import functools
from time import time


def uppercase(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()

    return wrapper


def measure_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'{func.__name__} executed in {end - start} seconds')
        return result

    return wrapper


def debug(func):
    """print func name with args, kwargs and result"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ', '.join(args)
        kwargs_str = ', '.join(f'{key}={value}' for (key, value) in kwargs.items())
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args_str}, {kwargs_str}) returned {result}')
        return result

    return wrapper


def cache(func):
    # internal_cache = {}
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = args + tuple(kwargs.values())
        # if cache_key not in internal_cache:
        if cache_key not in wrapper.internal_cache:
            wrapper.internal_cache[cache_key] = func(*args, **kwargs)
            # internal_cache[cache_key] = func(*args,  **kwargs)
        return wrapper.internal_cache[cache_key]
        # return   internal_cache[cache_key]

    wrapper.internal_cache = {}
    return wrapper


def repeat(count):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(count):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


# @debug
# @cache
def get_hello_message(name):
    return f'Hello, I am {name}'


@repeat(5)
def print_hello_message(name):
    print(get_hello_message(name))


print_hello_message('Maria')
# print_hello_message = repeat(3)(print_hello_message)


print(get_hello_message)
print(get_hello_message.__name__)


@debug
@uppercase
def get_current_temperature():
    return '3\' celsius'


get_current_temperature = debug(uppercase(get_current_temperature))


@measure_time
def big_loop():
    x = 0
    for _ in range(100000000):
        x += 1


@measure_time
@cache
def fibonacci(n):
    # print(f'Calculating F({n})')
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


@measure_time
def fibonacci2(n):
    # print(f'Calculating F({n})')
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci2(n - 1) + fibonacci2(n - 2)


print(get_hello_message('Pesho'))
print(get_current_temperature())
print(get_current_temperature)

print_hello_message('Gosho')

# big_loop()
# print(fibonacci(n=35))
# print(fibonacci2(n=35))

# print(fibonacci.internal_cache)
# print(get_hello_message.internal_cache)
# print(fibonacci.internal_cache)
# print(get_hello_message.internal_cache)
