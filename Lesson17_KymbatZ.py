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

'''#Fractions
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
print("Sum:", arithmetic_operation(row1, row2, "sum"))'''