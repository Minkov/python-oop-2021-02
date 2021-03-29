import csv
import io
import json
from abc import ABC, abstractmethod


class ServiceResult:
    def __init__(self, is_valid, errors):
        self.is_valid = is_valid
        self.errors = errors

    @classmethod
    def valid(cls):
        return cls(True, None)


print(ServiceResult(True, None))
print(ServiceResult.valid())


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_with_name(cls, name):
        return cls(name, 0)


class Parser(ABC):
    @abstractmethod
    def parse(self, obj):
        pass


class JsonParser(Parser):
    def parse(self, obj):
        return json.dumps(obj.__dict__)


class CsvParser(Parser):
    def parse(self, obj):
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(obj.__dict__.keys())
        writer.writerow(obj.__dict__.values())
        return output.getvalue()


class StringParser(Parser):
    def parse(self, obj):
        return str(obj)


class ParsersFactory:
    def get(self, format: str) -> Parser:
        if format == 'json':
            return JsonParser()
        elif format == 'csv':
            return CsvParser()
        else:
            return StringParser()


class ParsersSimpleFactory:
    def get_csv(self):
        return CsvParser()

    def get_json(self):
        return JsonParser()


pesho = Person('Pesho', 11)
parsers_factory = ParsersFactory()

format = input()

parser = parsers_factory.get(format)
result = parser.parse(pesho)

print(result)
