import BaseClasses as bc

employee1 = bc.Developer("Ray", 69, "Male", "React")
dev1 = bc.Developer("Mike", 78, "Female", "Java")

# Test that dev 1 inherited attributes from base and child class
dev1.set_framework("React")

# Get dev1 methods from the child class
print(dev1.get_Developer_Info())

# Checking if child is an instance of a superclass
print(isinstance(dev1, bc.Developer))
print(isinstance(dev1, bc.Tester))


# Check on class inheritance, calling super() method
print(dev1.messageOfTheDay())

# test the person type
person1 = bc.Tester("Ray", 69, "Male")
print(person1.name)
