from fractions import Fraction
from typing import List, Union

# Function to perform arithmetic operations
def arithmetic_operation(a, b, operation):
    if operation == "sum":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    else:
        raise ValueError("Operation not supported")

# Whole numbers
num1 = 5
num2 = 3
print("Whole Numbers:")
print("Sum:", arithmetic_operation(num1, num2, "sum"))
print("Subtraction:", arithmetic_operation(num1, num2, "subtract"))
print("Multiplication:", arithmetic_operation(num1,num2, "multiply"))

#Fractions
frac1 = Fraction(1, 2)
frac2 = Fraction(1, 3)
print("\nFractions:")
print("Sum:", arithmetic_operation(frac1, frac2, "sum"))
print("Subtraction:", arithmetic_operation(frac1, frac2, "subtract"))
print("Multiplication:", arithmetic_operation(frac1, frac2, "multiply"))

#Rows
row1 = [1.1, 2.2, 3.3]
row2 = [0.5, 1.0, 1.5]
print("\nRows (Lists):")
print("Sum:", arithmetic_operation(row1, row2, "sum"))
print("Subtraction:", arithmetic_operation(row1, row2, "subtract"))
print("Multiplication:", arithmetic_operation(row1, row2, "multiply"))

import math
class Shape:
    def area(self):
        pass # Placeholder method to be overridden in subclasses

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height
    
# Creating instances of shapes and calculating their areas
    circle = Circle(5)
    print(f"Area of Circle with radius 5: {circle.area()}")

    rectangle = Rectangle(4, 6)
    print(f"Area of Rectangle with width 4 and height 6: {rectangle.area()}")

    triangle = Triangle(3, 8)
    print(f"Area of Triangle with base 3 and height 8: {triangle.area()}")


from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Drawable):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        print(f"Drawing a circle with radius {self.radius}")

class Rectangle(Drawable):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def draw(self):
        print(f"Drawing a rectangle with width {self.width} and height {self.height}")

# Creating instances and calling draw method
circle = Circle(5)
circle.draw()

rectangle = Rectangle(4,6)
rectangle.draw()