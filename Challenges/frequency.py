"""
hallenge 3: Hashing Begins (VERY IMPORTANT FOR DSA)
Problem: Frequency Counter
Goal
Write a program that:
Takes n integers
Stores frequency of each number in a dictionary
Prints each number with its frequency
"""
n = int(input("Enter number of elements: "))
numbers = dict()
for i in range(n):
    element = int(input("Enter element: "))
    if element in numbers:
        numbers[element] += 1
    else:
        numbers[element] = 1
for key, value in numbers.items():
    print(f"{key}: {value}")
