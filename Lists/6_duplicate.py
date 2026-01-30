'''
Write a program to read a list of elements. Modify 
this list so that it does not contain any duplicate 
elements, i.e., all elements occurring multiple times 
in the list should appear only once.
'''
numbers = []
n = int(input("Enter the number of element: "))
for i in range(n):
    numbers.append(int(input("Enter the element: ")))
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
print("List:", numbers)
print("List after removing duplicates:", unique)