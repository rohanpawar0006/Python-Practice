"""
The program should ask for the position of 
the element to be deleted from the list. Write 
a function to delete the element at the desired 
position in the list.
"""
def delete_element(lst, position):
    if position < 1 or position > len(lst):
        return "Invalid position"
    position = position - 1
    lst.pop(position)
    return lst
numbers = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    numbers.append(int(input("Enter the element: ")))
print(numbers)
position = int(input("Enter the position to delete that value: "))
print(numbers)
print("List after deleting:", delete_element(numbers, position))

