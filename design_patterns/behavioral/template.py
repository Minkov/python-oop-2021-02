from abc import abstractmethod, ABC


class Employee:
    def __init__(self, first_name, last_name, job_title):
        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job_title

    def __repr__(self):
        return f'{self.first_name} {self.last_name}: {self.job_title}'


class EmployeesList(ABC):
    def __init__(self):
        self.employees = []

    @staticmethod
    @abstractmethod
    def order_by(x: Employee):
        pass

    def add_employee(self, employee: Employee):
        self.employees.append(employee)

    def list_employees(self):
        ordered_employees = sorted(self.employees, key=self.order_by)
        return ordered_employees


class EmployeesListByFirstName(EmployeesList):
    @staticmethod
    def order_by(x: Employee):
        return x.first_name


class EmployeesListByLastName(EmployeesList):
    @staticmethod
    def order_by(x: Employee):
        return x.last_name


el = EmployeesListByFirstName()
el.add_employee(Employee('Pesho', 'Georgiev', 'Software Developer'))
el.add_employee(Employee('Angel', 'Petrov', 'Manager'))
el.add_employee(Employee('Joro', 'Angelov', 'Human Resources'))

[print(e) for e in el.list_employees()]

el = EmployeesListByLastName()
el.add_employee(Employee('Pesho', 'Georgiev', 'Software Developer'))
el.add_employee(Employee('Angel', 'Petrov', 'Manager'))
el.add_employee(Employee('Joro', 'Angelov', 'Human Resources'))

[print(e) for e in el.list_employees()]
