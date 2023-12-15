import Shape as sh

mysquare = sh.Circle("Circle", "Blue", 5)
myWeirdShape = sh.Circle("WeirdShape", "Blue",5)

## Test super class method definition
print(mysquare.typeofShape())

## Test super class method - no shape defined
print(myWeirdShape.typeofShape())

## Test area of circle using inheritance
mycircle = sh.Circle("Circle","Blue", 5)
print(mycircle.area())

## Test we can't pass wrong value for diameter
mycircle2 = sh.Circle("Circle", "Red", "Don't know")
print(mycircle2.area())

## Test square area method
square1 = sh.Square("Square", "Yellow", 5)
print(square1.area())