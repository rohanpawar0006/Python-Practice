"""
Challenge 2: DSA Begins (Arrays + Loops)
Problem: Count Positive, Negative, and Zeros
Goal
Write a program that: Takes n integers from the user Stores them in a list
Counts:
Number of positive
Number of negative
Number of zeros
"""

n = int(input("Enter number of elements: "))
list1 = []
for i in range(n):
    list1.append(int(input("Enter element: ")))
positive = 0
negative = 0
zero = 0
for num in list1:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1
print("Positive: ", positive)
print("Negative: ", negative)
print("Zero: ", zero)
