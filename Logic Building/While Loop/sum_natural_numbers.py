# 6. Calculate and print the sum of the first n natural numbers. 
number = int(input("Enter a number: "))
n = 1
sumNum = 0
while n <= number:
    sumNum += n
    n += 1
print(sumNum)