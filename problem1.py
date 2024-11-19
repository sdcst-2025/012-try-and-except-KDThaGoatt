#python3
# Quadratic Equation
# Have the user enter in the coefficients of a quadratic equation in the
# format: ax^2 + bx + c = 0 and calculate the solutions of the equation
# rounded to 2 decimal places. Use a try...except block to catch if there
# is no solution


""" Sample output:
Enter in the coefficients for a quadratic equation in the format:
  ax^2 + bx + c = 0
a:3
b:d
c:1
Those are not valid values for a, b or c
a:3
b:2
c:1
There are no real roots to the equation
a:2
b:-3
c:-6
The roots are 2.64 and -1.14
a:1
b:8
c:16
The roots are -4.0 and -4.0
"""
import os
os.system('cls')
import math

print("Enter in the coefficients for a quadratic equation in the format:")
print("  ax^2 + bx + c = 0")

a = (input("a = "))
b = (input("b = "))
c = (input("c = "))

try:
    a = float(a)
    b = float(b)
    c = float(c)
    firstEq = (-b + math.sqrt(b ** 2 - 4*a*c)) / (2*a)
    secondEq = (-b - math.sqrt(b ** 2 - 4*a*c)) / (2*a)
    roundOne = round(firstEq, 2)
    roundTwo = round(secondEq, 2)
    print(f"The roots are {roundOne} and {roundTwo}")
except:
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        print("There are no real roots to the equation")

    except:
        print("Those are not valid values for a, b or c")
