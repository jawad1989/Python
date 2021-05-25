class Employee():
    company = "TCS"
    def __init__(self, id=None, salary=0, department=None) -> None:
        self.ID     = id
        self.salary = salary
        self.department = department
    # ID = None
    # salary = 3000
    # department = 'IT'

emp = Employee()
print(emp.company)
