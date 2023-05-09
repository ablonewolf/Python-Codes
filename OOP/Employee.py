class Employee:
    active_employee = 0

    def __init__(self, name, employee_id, age):
        self.name = name
        self.employee_id = employee_id
        self._age = age
        Employee.active_employee +=  1

    def __repr__(self):
        return f"{self.name} is an employee with ID no: {self.employee_id}. This employee is {self.age} years old. "

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age >= 0:
            self._age = age
        else:
            self._age = 0

    @classmethod
    def get_active_employees(cls):
        return cls.active_employee

    @classmethod
    def user_from_string(cls, data_string):
        name, employee_id, age = data_string.split(',')
        return cls(name, employee_id, age)


Arka = Employee("Arka Bhuiyan", 99178, "25")
Farhan = Employee("Farhan Zaman", 11514, "25")
print(f"Current number of total active employees is {Employee.get_active_employees()}")
Nipa = Employee("Nipa Howladar", 11513, "26")
Akif = Employee("Akif Azwad", 11507, "26")
print(f"Current number of total active employees is {Employee.get_active_employees()}")

Mosfik = Employee.user_from_string("Mosfikur Rahman,11502,26")
print(f"Current number of total active employees is {Employee.get_active_employees()}")
print(Arka)
print(Farhan)
print(Nipa)
print(Akif)
print(Mosfik)

