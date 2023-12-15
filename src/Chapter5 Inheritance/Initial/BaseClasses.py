
class Person:
    def __init__(self, name, age, gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    def messageOfTheDay(self):
        return "Welcome to this class"

class Developer(Person):
    def __init__(self, name, age, gender, framework) -> None:
        super().__init__(name, age, gender)
        self.framework = framework

    def set_framework(self, framework):
        self.framework = framework

    def get_framwork(self):
        return self.framework
    
    def get_Developer_Info(self):
        return f"The dev name is: {self.name} and the role is {self.framework}"


    def messageOfTheDay(self):
           return super().messageOfTheDay()

class Tester(Person):
    def set_framework(self, framework):
        self.framework = framework

    def get_framwork(self):
        return self.framework
    
    def get_Tester_Info(self):
        return f"The tester name is: {self.name} and the role is {self.framework}"

    def messageOfTheDay(self):
        return super().messageOfTheDay()