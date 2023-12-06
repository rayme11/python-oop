import employee

e1 = employee.Employee("Ray", "Consumer", 69, 10000, 2, 10)
e2 = employee.Employee("Karen", "Consumer", 69, 10000, 2, 10)
e3 = employee.Employee("Oray", "Consumer", 69, 10000, 2, 10)
e4 = employee.Employee("Isa", "Consumer", 69, 10000, 2, 10)
e5 = employee.Employee("Mayra", "Consumer", 69, 10000, 2, 10)

employees = [e1, e2, e3, e4, e5]

for employee in employees:
    print(employee.name)
    print(employee.__class__)
