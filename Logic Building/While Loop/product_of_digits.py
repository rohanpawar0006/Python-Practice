# 10. Find and print the product of all digits of a given number.
number = int(input("Enter a number: "))
product = 1
num = 1
while number:
    num = number % 10
    product *= num
    number = number // 10
print(product)