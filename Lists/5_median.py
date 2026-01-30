"""
Write a program to read a list of n integers and find 
their median. 
Note: The median value of a list of values is the 
middle one when they are arranged in order. If there 
are two middle values then take their average. 
Hint: You can use an built-in function to sort the list
"""
def median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 1:
        return numbers[n//2]
    else:
        mid1 = numbers[n//2 - 1]
        mid2 = numbers[n//2]
        return (mid1+mid2)/2
    
numbers = []
n = int(input("Enter the numbers of elements: "))
for i in range(n):
    numbers.append(int(input("Enter the element: ")))
print("Median of the list is: ", median(numbers))

