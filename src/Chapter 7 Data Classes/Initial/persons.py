class Person:
    def __init__(self, name, age, project) -> None:
        self.name = name
        self.age = age
        self.project = project

    def __str__(self) -> str:
        return f"name={repr(self.name)}, age={repr(self.age)}"

   


class Project:
    def __init__(self, name, cost, company) -> None:
        self.name = name
        self.cost = cost
        self.company = company

    
    def  __str__(self) -> str:
        return f"This person works in project: (name={repr(self.name)}, cost={repr(self.cost)}, company={repr(self.company)})"