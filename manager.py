#Create a python program to show how manager class inherits attributes and methods from both Person and Employee,
#and how we can add additional behaviours and properties in the Manager class.Person class :contains common attributes like name and age.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print("Name:", self.name, "| Age:", self.age)

class Employee:
    def __init__(self, employee_id, department):
        self.employee_id = employee_id
        self.department = department

    def display_employee_info(self):
        print("Employee ID:", self.employee_id, "| Department:", self.department)

class Manager(Person, Employee):
    def __init__(self, name, age, employee_id, department, team_size):
        Person.__init__(self, name, age)
        Employee.__init__(self, employee_id, department)
        self.team_size = team_size

    def display_manager_info(self):
        self.display_person_info()
        self.display_employee_info()

person1 = Person("A", 30)
person1.display_person_info()

employee1 = Employee("E1", "HR")
employee1.display_employee_info()

manager1 = Manager("B", 40, "M1", "IT", 5)
manager1.display_manager_info()