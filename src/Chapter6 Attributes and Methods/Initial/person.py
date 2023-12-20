class Person:
    minimum_age = 21

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @classmethod
    def change_min_age(cls, new_age):
        if new_age < 21:
            raise ValueError("Only adults >= 21 are permitted in this class!! ")
        cls.minimum_age = new_age

    def get_minimum_age(self):
        return "The minimum age for the class is: " + str(self.minimum_age)

    def get_name(self):
        return "Hello: " + self.name

    def get_age(self):
        return "Your age is: " + str(self.age)
    
    

