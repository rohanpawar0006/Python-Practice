# 9. Calculate and print the factorial of a given number. 
number = int(input("Enter a number: "))
n = 1
factNum = 1
while n <= number:
    factNum *= n
    n += 1
print(factNum)