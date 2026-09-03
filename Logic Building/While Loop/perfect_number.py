# 16. Check whether the given number is a Perfect number. 
number = int(input("Enter a number: "))
sumNum = 0
n = 1
while n < number:
    if number % n == 0:
        sumNum += n
    n += 1
if sumNum == number:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
    