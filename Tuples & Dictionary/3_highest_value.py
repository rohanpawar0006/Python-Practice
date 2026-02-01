""" 
Write a Python program to find the highest 2 values 
in a dictionary.
"""

n = int(input("Enter the numbers of values to insert in dictionary: "))
number = dict()
count = 1
while count <= n:
    key = input("Enter the key name for the value: ")
    value = int(input("Enter the value: "))
    number[key] = value
    count += 1
values = list(number.values())
values.sort(reverse=True)
highest = values[0]
second_highest = values[1]
print(number)
print(values)
print("Highest value: ", highest)
print("Second Highest value: ", second_highest)

