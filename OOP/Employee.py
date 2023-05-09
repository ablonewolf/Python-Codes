class Employee:
    active_employee = 0

    def __init__(self, name, employee_id, programming_language):
        self.name = name
        self.employee_id = employee_id
        self.programming_language = programming_language
        Employee.active_employee += 1

    def __repr__(self):
        return f"{self.name} is an employee with ID no: {self.employee_id}. This employee prefers " \
               f"{self.programming_language} as his primary programming language."

    def print_info(self):
        print(f"Name of the employee: {self.name}, employee ID: {self.employee_id} and his preferred programming "
              f"language is {self.programming_language}")

    @classmethod
    def get_active_employees(cls):
        return cls.active_employee

    @classmethod
    def user_from_string(cls, data_string):
        name, employee_id, programming_language = data_string.split(',')
        return cls(name, employee_id, programming_language)


Arka = Employee("Arka Bhuiyan", 99178, "Java")
Farhan = Employee("Farhan Zaman", 11514, "JavaScript")
print(f"Current number of total active employees is {Employee.get_active_employees()}")
Nipa = Employee("Nipa Howladar", 11513, "Java")
Akif = Employee("Akif Azwad", 11507, "Python")
print(f"Current number of total active employees is {Employee.get_active_employees()}")

Mosfik = Employee.user_from_string("Mosfikur Rahman,11502,Java")
print(f"Current number of total active employees is {Employee.get_active_employees()}")
print(Arka)
Arka.print_info()
print(Farhan)
Farhan.print_info()
print(Nipa)
Nipa.print_info()
print(Akif)
Akif.print_info()
print(Mosfik)
Mosfik.print_info()
