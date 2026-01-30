num1 = int(input("Entet first number: "))
num2 = int(input("Entet second number: "))

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
#OR
num1, num2 = num2, num1
print(num1, num2)