# 13. Check whether the given number is a palindrome.

number = int(input("Enter a number: "))
reverse = 0
original = number
val = 0
while number > 0:
    val = number % 10
    reverse = (reverse * 10) + val
    number = number // 10
if reverse == original:
    print("Its palindrome")
else:
    print("Not a palindrome")
