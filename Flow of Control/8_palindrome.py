number = input("Enter the Number: ")
rev = ""
for i in number:
    rev = i + rev
if number == rev:
    print("It's a Palindrome")
else:
    print("It's Not a Palindrome")
