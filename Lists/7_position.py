"""Write a program to read a list of elements. Input 
an element from the user that has to be inserted in 
the list. Also input the position at which it is to be 
inserted. Write a user defined function to insert the 
element at the desired position in the list.
"""
def insert_element(lst, element, position):
    position = position - 1
    lst.insert(position, element)
    return lst
numbers = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    numbers.append(int(input("Enter the element: ")))
print(numbers)
element = int(input("Enter the element to be inserted: "))
position = int(input("Enter the position: "))
print("List after insertion:", insert_element(numbers, element, position))
