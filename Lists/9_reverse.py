"""
Read a list of n elements. Pass this list to a function 
which reverses this list in-place without creating a 
new list.
"""
"""
numbers = []
n = int(input("Enter the number of element: "))
for i in range(n):
    numbers.append(int(input("Enter the element: ")))
print("Your list: ", numbers)
print("After reversing: ", numbers[::-1])
"""
def reverse(numbers):
    start = 0
    end = len(numbers) - 1
    while start < end:
        numbers[start], numbers[end] = numbers[end], numbers[start]
        start += 1
        end -= 1
numbers = []
n = int(input("Enter the number of element: "))
for i in range(n):
    numbers.append(int(input("Enter the element: ")))
print("Your list: ", numbers)
reverse(numbers)
print("After reversing: ", numbers)
