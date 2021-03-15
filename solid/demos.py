from abc import ABC, abstractmethod


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def get_name(self):
        return self.name


# The beginning
# class StudentTaxes(ABC):
#     def __init__(self, student, semester_tax):
#         self.student = student
#         self.semester_tax = semester_tax
#
#     @abstractmethod
#     def get_student_discount(self):
#         pass


class StudentTaxes:
    def __init__(self, student, semester_tax):
        self.student = student
        self.semester_tax = semester_tax

    def get_student_discount(self):
        return 0


# Later add this
class ExcellentStudentTaxes(StudentTaxes):
    def get_student_discount(self):
        if self.student.grade >= 5:
            return self.semester_tax * 0.4
        return 0


# Later still add this
class GoodStudentTaxes(StudentTaxes):
    def get_student_discount(self):
        if self.student.grade >= 4:
            return self.semester_tax * 0.2
        return 0


class InlvalidStudentTaxes(StudentTaxes):
    def get_student_discount(self):
        raise TypeError()


# Violation
# class Formatter:
#     def format_name(self, student):
#         return f'Name: {student.name}'
#
#     def format_name_and_grade(self, student):
#         return f'Name: {student.name}, Grade: {student.grade}'

class Formatter(ABC):
    @abstractmethod
    def format(self, student):
        pass


class NameFormatter(Formatter):
    def format(self, student):
        return f'Name: {student.name}'


class NameAndGradeFormatter(Formatter):
    def format(self, student):
        return f'Name: {student.name}, Grade: {student.grade}'


class StudentRegistry:
    def __init__(self):
        self.students = []
        # self.formatter = formatter

    def register(self, student):
        self.students.append(student)

    def unregister(self, student):
        self.students.pop(self.students.index(student))

    # def print_registered(self):
    #     for student in self.students:
    #         print(self.formatter.format(student))

    # Also fine
    def print_registered(self, formatter: Formatter):
        for student in self.students:
            print(formatter.format(student))


sr = StudentRegistry()

st1 = Student('Gosho', 5.5)
st2 = Student('Pesho', 4)

print(ExcellentStudentTaxes(st1, 100).get_student_discount())
print(GoodStudentTaxes(st1, 100).get_student_discount())

print(ExcellentStudentTaxes(st2, 100).get_student_discount())
print(GoodStudentTaxes(st2, 100).get_student_discount())
sr.register(st1)
sr.register(st2)
sr.print_registered(NameFormatter())
sr.print_registered(NameAndGradeFormatter())
# sr.register()
# sr.print_students()
