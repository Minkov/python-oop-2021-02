# def cache(func):
#     # internal_cache = {}
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         cache_key = args + tuple(kwargs.values())
#         # if cache_key not in internal_cache:
#         if cache_key not in wrapper.internal_cache:
#             wrapper.internal_cache[cache_key] = func(*args, **kwargs)
#             # internal_cache[cache_key] = func(*args,  **kwargs)
#         return wrapper.internal_cache[cache_key]
#         # return   internal_cache[cache_key]
#
#     wrapper.internal_cache = {}
#     return wrapper
import functools


class cache:
    def __init__(self, func):
        self.func = func
        self.internal_cache = {}

    def __call__(self, *args, **kwargs):
        cache_key = args + tuple(kwargs.values())
        if cache_key not in self.internal_cache:
            self.internal_cache[cache_key] = self.func(*args, **kwargs)
        return self.internal_cache[cache_key]


class uppercase:
    def __init__(self, func):
        self.func = func
        functools.update_wrapper(self, self.func)

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs).upper()


def repeat(count):
    class decorator:
        def __init__(self, func):
            self.func = func

        def __call__(self, *args, **kwargs):
            for _ in range(count):
                self.func(*args, **kwargs)

    return decorator


class logger:
    log_file_path = './log.txt'

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        args_str = ', '.join(args)
        kwargs_str = ', '.join(f'{key}={value}' for (key, value) in kwargs.items())
        result = self.func(*args, **kwargs)
        with open(self.log_file_path, 'a') as file:
            file.write(f'{self.func.__name__}({args_str}, {kwargs_str}) returned {result}\n')
        return result


@logger
@uppercase
def get_message():
    return 'H asdasd'


@repeat(17)
def print_something():
    print('Hello')


print(get_message())
print_something()
