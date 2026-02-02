"""
Write a code where you use the wrong number of 
arguments for a method (say sqrt() or pow()). Use the 
exception handling process to catch the ValueError 
exception.
"""
from math import sqrt, pow
try:
    sqaure_root = int(input("Enter a number to find Square root of it: "))
    print("The Square Root of ", sqaure_root, "is ", sqrt(sqaure_root))
    power = int(input("Enter the number to find Power of it: "))
    print("The Power of the given number ", power, "is ", pow(power,2))
except TypeError:
    print("TypeError: Wrong number of arguments used")
