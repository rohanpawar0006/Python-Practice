# 18. Check whether the given number is a prime number. 
num = int(input("Enter a number: "))

divisor = 2

while divisor < num:
    if num % divisor == 0:
        print("Not Prime")
        break
    divisor += 1
else:
    print("Prime")