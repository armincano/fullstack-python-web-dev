"""
1. Design a new user-defined exception class.
2. This class should handle the input value of a variable called salary.
3. Ensure that the salary value is between 1000 and 2000.
4. If the salary value is not within this range, raise an exception.
5. The exception should indicate that the salary is not within the range of 1000 to 2000.
"""
class SalaryNotInRange(Exception):
    def __init__(self, message="The salary must be between 1000 and 2000"):
        self.__message = message
        super().__init__(self.__message)
        
salary = None
while True:
    try:
        input_salary = int(input("Enter a salary: "))
        if input_salary not in range(1000,2001):
            raise SalaryNotInRange
        salary = input_salary
        break
    except SalaryNotInRange as e:
        print(e)
    except ValueError:
        print("The input salary must be an integer.")
print(f"The salary is {salary}")