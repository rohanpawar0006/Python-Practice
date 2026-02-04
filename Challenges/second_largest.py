"""
Problem: Second Largest Element
Goal
Write a function:
def second_largest(arr):
That returns the second largest distinct element in the list.
Then:
Take list input from user
Call the function
Print the result
Constraints
List has at least 2 elements
Do NOT use:
sort()
max() more than once
Time complexity: O(n)
"""
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
print(secLarge(numbers))
"""  
def second_largest(arr):
    largest = None
    second = None
    for num in arr:
        if largest is None or num > largest:
            if num != largest:
                second = largest
            largest = num
        elif num != largest and (second is None or num > second):
            second = num
    return second
result = second_largest(numbers)
if result is None:
    print("No second largest")
else:
    print(result)


Score: 8.5 / 10
Rubric:
Algorithm: 9.5/10
Efficiency: 10/10
Edge cases: 6.5/10
Interview readiness: 8.5/10
"""