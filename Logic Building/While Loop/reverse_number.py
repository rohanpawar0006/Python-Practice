# 12. Reverse the given number and print the reversed value. 
number = (input("Enter a number: "))
reverse = ""
val = 0
while number:
    val = int(number) % 10
    reverse += str(val)
    number = int(number) // 10
print(reverse)
