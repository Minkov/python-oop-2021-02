import json


class School:
    def __init__(self, name, students):
        self.students = students
        self.name = name

    def __repr__(self):
        return str(self.__dict__)

    @classmethod
    def from_string(cls, school_string):
        index = school_string.index(':')
        name = school_string[:index]
        students = school_string[index + 1:].split(', ')
        return cls(name, students)

    @classmethod
    def from_json(cls, school_json):
        school_dict = json.loads(school_json)
        return cls(school_dict['name'], school_dict['students'])
        # return School(attrs['name'], attrs['students'])


print(School('SoftUni', ['Sofi', 'Marta', 'Pesho']))

print(School.from_string('Softuni: Sofi, Marta, Pesho'))
print(School.from_json('''
{
    "name": "SoftUni",
    "students": [
        "Sofi",
        "Marta",
        "Pesho"
    ]
}
'''))
