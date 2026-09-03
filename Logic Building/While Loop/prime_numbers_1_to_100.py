# 17. Print all prime numbers between 1 and 100.
num = 2
while num <= 100:
    divisor = 2
    while divisor < num:
        if num % divisor == 0:
            break
        divisor += 1
    else:
        print(num)
    num += 1