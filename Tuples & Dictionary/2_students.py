"""
Write a program to input names of n students and 
store them in a tuple. Also, input a name from the 
user and find if this student is present in the tuple or not.
Rationalised 2023-24
TUPLES AND DICTIONARIES
225
We can accomplish these by:
(a) writing a user defined function 
(b) using the built-in function
"""
def studentPresent(name):
    if name in student_names:
        print(f"{name} is present in the list!")
    else:
        print(f"{name} is not present in the list!")
n = int(input("Enter the number of students in list: "))
names = []
for i in range(n):
    names.append(input("Enter the name of student: "))
student_names = tuple(names)
for name in student_names:
    print("List of Students: ", name)
name = input("Enter name of student to check in the list: ")
studentPresent(name)
