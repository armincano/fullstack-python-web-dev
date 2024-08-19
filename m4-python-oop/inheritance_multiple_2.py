class Person:
    def __init__(self, name, last_name, year):
        self.name = name
        self.last_name = last_name
        self.year = year

class Department:
    def __init__(self, department_name, department_short_name):
        self.department_name = department_name
        self.department_short_name = department_short_name

class Worker(Person, Department):
    def __init__(self, name, last_name, year, department_name, department_short_name, salary):
        Person.__init__(self, name, last_name, year)
        Department.__init__(self, department_name, department_short_name)
        self.salary = salary
    def __dict__(self):
        return {
            "name": self.name,
            "last_name": self.last_name,
            "year": self.year,
            "department_name": self.department_name,
            "department_short_name": self.department_short_name,
            "salary": self.salary
        }
        
class Student:
    pass

worker_1 = Worker("Juan", "Pérez", 2005, "Ingeniería de software", "IS", 20000)
print(worker_1.__dict__())

is_worker_1_instance_of_person = isinstance(worker_1, Worker)
is_worker_1_instance_of_department = isinstance(worker_1, Worker)
is_worker_1_instance_of_worker = isinstance(worker_1, Worker)
is_worker_1_instance_of_student = isinstance(worker_1, Student)

print(f"Is worker_1 instance of Person: {is_worker_1_instance_of_person}")
print(f"Is worker_1 instance of Department: {is_worker_1_instance_of_department}")
print(f"Is worker_1 instance of Worker: {is_worker_1_instance_of_worker}")
print(f"Is worker_1 instance of Student: {is_worker_1_instance_of_student}")