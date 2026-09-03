# 11. Count and print the total number of digits in a given number. 
number = int(input("Enter a number: "))
count = 0
while number:
    number = number // 10 
    count += 1
print(count)