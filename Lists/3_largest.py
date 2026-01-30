'''Write a function that returns the largest element of 
the list passed as parameter.
'''
numbers = []
n = int(input("Enter the number of element in list: "))
for i in range(n):
    numbers.append(int(input("Enter the element: ")))
print(numbers)

print("Largest element: ", max(numbers))