'''
Write a function to return the second largest number 
from a list of numbers.
'''
def secLarge(numbers):
    larg = numbers[0]
    seclarge = numbers[0]
    for num in numbers:
        if num > larg:
            seclarge = larg
            larg = num
        elif num > seclarge and num != larg:
            seclarge = num
    return seclarge
numbers = []
n = int(input("Enter the number of elements: "))  
for i in range(n):
    numbers.append(int(input("Enter the elements: ")))
print(numbers)
print("Second largest number:", secLarge(numbers))