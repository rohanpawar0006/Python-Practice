'''Write a program to find the number of times an 
element occurs in the list.'''

list1 = []
n = int(input("Enter all your number: "))

for i in range(n):
    list1.append(int(input("Enter element: ")))

num = int(input("Enter the Number which you want to count: "))
print(list1)
print(f"The No. of times {num} is repeated is {list1.count(num)}")
