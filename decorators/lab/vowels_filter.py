def vowel_filter(func):
    vowels = set('aeiou' + 'aeiou'.upper())

    def wrapper():
        result = func()
        return [c for c in result if c in vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


@vowel_filter
def get_hello_message():
    return f'Hello, I am Pesho'


@vowel_filter
def get_current_temperature():
    return '3\' celsius'


print(get_letters())
print(get_hello_message())
print(get_current_temperature())
