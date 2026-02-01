""" 
Write a program to input your friends’s names and their Phone Numbers and store them in the  
dictionary as the key-value pair. Perform the following operations on the dictionary:
a) Display the name and phone number of all your friends
b) Add a new key-value pair in this dictionary and display the modified dictionary
c) Delete a particular friend from the dictionary
d) Modify the phone number of an existing friend
e) Check if a friend is present in the dictionary or not
f) Display the dictionary in sorted order of names
"""
n = int(input("Enter the Number of friend's name to add in list: "))
count = 1
friend_list = dict()
while count <= n:
    name = input("Enter friend name: ")
    phone = input(f"Enter {name}'s Phone Number: ")
    friend_list[name] = phone
    count += 1
print("a) Display the name and phone number of all your friends")
print("b) Add a new key-value pair in this dictionary and display the modified dictionary")
print("c) Delete a particular friend from the dictionary")
print("d) Modify the phone number of an existing friend")
print("e) Check if a friend is present in the dictionary or not")
print("f) Display the dictionary in sorted order of names")
option = input("Enter your operation: ")
if option == "a":
    print(friend_list)
elif option == "b":
    n2 = int(input("Enter the Number of friend's name to add in list: "))
    count2 = 1
    list2 = dict()
    while count2 <= n2:
        name2 = input("Enter friend name: ")
        phone2 = input(f"Enter {name}'s Phone Number: ")
        list2[name2] = phone2
        count2 += 1
    friend_list.update(list2)
    print(friend_list)
elif option == "c":
    name = input("Enter the name of friend to delete from the dictionary: ")
    del friend_list[name]
    print(friend_list)
elif option == "d":
    name = input("Enter friend name to modify phone number: ")
    if name in friend_list:
        new_phone = input("Enter new phone number: ")
        friend_list[name] = new_phone
        print(friend_list)
    else:
        print("Friend not found!")
elif option == "e":
    name = input("Enter friend name to search: ")
    if name in friend_list:
        print(f"{name} is present with phone number {friend_list[name]}")
    else:
        print(f"{name} is not present in the dictionary")
elif option == "f":
    print("Friends list in sorted order:")
    for name in sorted(friend_list):
        print(name, ":", friend_list[name])
else:
    print("Please enter correct option from above list: ")
