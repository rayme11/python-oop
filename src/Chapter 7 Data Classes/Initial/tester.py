import persons as persons


project1 = persons.Project("Java", 500000,"KW")
person1 = persons.Person("Ray", 69, project1)

#Calling data classes and printing content
print(person1)
print(person1.project)