"""
    The program should ask for the value of the 
element to be deleted from the list. Write a 
function to delete the element of this value 
from the list.
"""
def delete_element(lst, element):
    if element in lst:
        lst.remove(element)
        return lst
    else:
        return "Element not found in the list"
numbers = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    numbers.append(int(input("Enter the element: ")))
print(numbers)
element = int(input("Enter the element to be delete: "))
print("List after delete:", delete_element(numbers, element))
