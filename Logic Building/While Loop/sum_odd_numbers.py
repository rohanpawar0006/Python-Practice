# 8. Calculate the sum of all odd numbers from 1 up to n. 
number = int(input("Enter a number: "))
sumNum = 0
n = 0
while n <= number:
    if n % 2 != 0:
        sumNum += n
    n += 1
print(sumNum)