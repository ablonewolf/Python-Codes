class Employee:
    def __init__(self, name, employee_id, programming_language):
        self.name = name
        self.employee_id = employee_id
        self.programming_language = programming_language

    def print_info(self):
        print(f"Name of the employee: {self.name}, employee ID: {self.employee_id} and his preferred programming "
              f"language is {self.programming_language}")


Arka = Employee("Arka Bhuiyan", 99178, "Java")
Arka.print_info()
