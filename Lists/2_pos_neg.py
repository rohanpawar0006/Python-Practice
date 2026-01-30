"""Write a program to read a list of n integers (positive
as well as negative). Create two new lists, one 
having all positive numbers and the other having 
all negative numbers from the given list. Print all 
three lists."""
numbers = []
positive = []
negative = []
n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)
for num in numbers:
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)
print(numbers)
print(positive)
print(negative)
