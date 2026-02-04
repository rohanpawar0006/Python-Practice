"""
Challenge 8: Prefix Thinking (Next Level)
Problem: Running Sum of an Array
Goal
Write a function:
def running_sum(arr):
That returns a new list where:
Each element at index i
Is the sum of elements from index 0 to i
"""
def running_sum(arr):
    running_arr = []
    x = 0
    for i in arr:
        x += i
        running_arr.append(x)
    return running_arr
numbers = []
n = int(input("Enter number of elements: "))
for i in range(n):
    numbers.append(int(input("Enter element: ")))
print(running_sum(numbers))

""" 
Score: 9 / 10
Rubric:
Algorithm & logic: 10/10
Time complexity: 10/10
Readability: 9/10
Syntax accuracy: 7/10 (small typo)
"""
