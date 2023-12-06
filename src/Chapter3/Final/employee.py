class Employee:
    def __init__(self, name, dept, age, salary, yearsOfService, increasePercentage) -> None:
        self.name = name
        self.dept = dept
        self.age = age
        self.salary = salary
        self.yearsOfService = yearsOfService
        self.increasePercentage = increasePercentage

    def salary_increase(self):
        self.salary += self.salary * (self.increasePercentage / 100)
        return self.salary
    
    def __str__(self) -> str:
        return f"{self.name} from {self.dept} makes a total salary to {self.salary}"
    
    def __repr__(self) -> str:
        return f"Employee({self.name},{self.dept},{self.salary})"
