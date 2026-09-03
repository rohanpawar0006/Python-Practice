# 14. Find and print the sum of digits of the given number. 
number = int(input("Enter a number: "))
sumNum = 0
num = 0
while number:
    num = number % 10
    sumNum += num
    number = number // 10
print(sumNum)