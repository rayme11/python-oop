def init_employee(name: str, dept: str, age: int, salary: float, yearsOfService: int, increasePercentage: int):
    return {
        "name": name,
        "dept": dept,
        "age": age,
        "salary": salary,
        "yearsOfService": yearsOfService,
        "increasePercentage": increasePercentage
    }

employee1 = init_employee("Ray", "Consumer", 69, 10000, 2, 10)
employee2 = init_employee("Karen", "UT", 23, 3000.99, 2,5)
employee3 = init_employee("Oray", "Rouse", 23, 5000.99, 2,10)
employee4 = init_employee("Isabel", "MiddleSchool", 23, 3000.99, 2,10)

employees = [employee1, employee2, employee3, employee4]

def salary_increase(employee):
    employee['salary'] += employee['salary'] * (employee['increasePercentage'] / 100)
    return employee['salary']


def print_employee(employee):
    print(f"{employee['name']} -- from dept: {employee['dept']} -- has a salary of {employee['salary']}")
    print("And with the salary increase the total salary will be: " + str(salary_increase(employee)) )
    

for employee in employees:
    print_employee(employee)