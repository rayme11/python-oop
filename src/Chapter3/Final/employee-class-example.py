import employee

e1 = employee.Employee("Ray", "Consumer", 69, 10000, 2, 10)
e2 = employee.Employee("Karen", "Consumer", 69, 50000, 2, 10)
e3 = employee.Employee("Oray", "Consumer", 69, 10000, 2, 10)
e4 = employee.Employee("Isa", "Consumer", 69, 10000, 2, 10)
e5 = employee.Employee("Mayra", "Consumer", 69, 20000, 2, 10)

employees = [e1, e2, e3, e4, e5]

for employee in employees:
    print(employee.name)
    print(employee.__class__)

print('Normal salary for e1 will be' + str(e1.salary))
e1.salary_increase()
print('Normal salary + increase will be for e1: ' + str(e1.salary))


print('Normal salary for e2 will be' + str(e2.salary))
e2.salary_increase()
print('Normal salary + increase will be for e2: ' + str(e2.salary))

##Optionally increase each employee salary
for e in employees:
    e.salary_increase()
    print('Salary for: ' + e.name + ' will be a total of: ' + str(e.salary))


##Calling the __str__ function from employee class
for e in employees:
   print(e)

##Using repr for debugging / dev purposes
print(repr(e1))



   



