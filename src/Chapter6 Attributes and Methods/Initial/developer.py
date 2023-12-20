import person as person

dev1 = person.Person("Ray", 41, "Male")

print(dev1.get_name())
print(dev1.get_age())

##Test changing a class property through class method
##shall fail validation
#dev1.change_min_age(15)

##Test changing a class property through class method
##shall pass validation
dev1.change_min_age(22)
print(dev1.get_minimum_age())