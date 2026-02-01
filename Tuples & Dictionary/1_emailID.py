"""
Write a program to read email IDs of n number of 
students and store them in a tuple. Create two new 
tuples, one to store only the usernames from the 
email IDs and second to store domain names from 
the email IDs. Print all three tuples at the end of the 
program. [Hint: You may use the function split()]
"""
n = int(input("Enter the numbers of EmailIDs to store: "))
email_list = []
for i in range(n):
    email_list.append(input("Enter the EmailID: "))
emails = tuple(email_list)
username= []
domain = []
for email in emails:
    part = email.split("@")
    username.append(part[0])
    domain.append(part[1])
username = tuple(username)
domain = tuple(domain)
print("Email IDs are: ", emails)
print("Username of Emails: ", username)
print("Domain of EmailID: ", domain)
