"""
Warmup 1 — Pure Logic (No tricks)
Problem:
You are given a list of integers.
👉 Return True if the list is strictly increasing.
👉 Otherwise return False.
Strictly increasing means:
Every element must be greater than the previous one.
"""
def is_strictly_increasing(arr):
    for i in range(len(arr)-1):
        if arr[i] >= arr[i+1]:
            return False
        if arr[i] < arr[i+1]:
            i+=1
        return True
n = int(input("Enter number of elements in list: "))
arr = []
for i in range(n):
    num = int(input("Enter the number: "))
    arr.append(num)
result = is_strictly_increasing(arr)
print(result)
