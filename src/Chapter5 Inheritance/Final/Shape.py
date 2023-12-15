""" Create a hierarchy of classes to represent different shapes. The base class should be Shape, 
and it should have attributes representing common properties of shapes, such as color. Additionally, 
it should have a method area that returns the area of the shape. 
Derive two classes from Shape: Circle and Rectangle. 
Each derived class should have its own attributes and methods. """

import math


class Shape:
    def __init__(self, figure, color) -> None:
        self.figure = figure
        self.color = color

    def typeofShape(self):
        if self.figure == "Circle":
            return "I am a circle "
        elif self.figure == "Square":
            return "I am a square "
        else:
            return "I don't have a shape "
        

class Circle(Shape):
    def __init__(self, figure, color, diameter) -> None:
        super().__init__(figure, color)
        self.diameter = diameter

    def area(self):
        if not isinstance(self.diameter, int):
             return "You can't calculate that"
        else:
            return self.typeofShape() + str(3.14 * (self.diameter/2) ** 2) + " in size"



class Square(Shape):
    def __init__(self, figure, color,lengthSide) -> None:
        super().__init__(figure, color)
        self.lengthSide = lengthSide

    def area(self):
        if not isinstance(self.lengthSide, int):
             return "You can't calculate that"
        else:
            return self.typeofShape() + str(self.lengthSide * self.lengthSide) + " in size"
        
