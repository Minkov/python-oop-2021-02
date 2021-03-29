def singleton(cls):
    instance = None

    def wrapper(*args, **kwargs):
        nonlocal instance
        if not instance:
            instance = cls(*args, **kwargs)
        return instance

    return wrapper


class JsonParser:
    def parse(self, obj):
        return f'json: {str(obj)}'


@singleton
class JsonParser2:
    def parse(self, obj):
        return f'json: {str(obj)}'


jp1 = JsonParser()
jp2 = JsonParser()

jp21 = JsonParser2()
jp22 = JsonParser2()
print(jp1)
print(jp2)
print(jp21)
print(jp22)
