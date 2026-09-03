# 15. Check whether the given number is an Armstrong number. 
number = int(input("Enter a number: "))
pow = 0
arms = 0
val = 0
original = number1 = number
while number:
    val = number % 10
    pow += 1
    number = number // 10
while number1:
    val = number1 % 10
    arms += val**pow
    number1 = number1 // 10
if original == arms:
    print("ArmStrong Number")
else:
    print("Not")