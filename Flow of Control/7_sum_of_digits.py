num = int(input("Enter an integer number: "))

sum_digits = 0
temp = abs(num)   # handles negative numbers

while temp > 0:
    digit = temp % 10
    sum_digits = sum_digits + digit
    temp = temp // 10

print("The sum of digits is:", sum_digits)
