name = input("Student enter your name: ")
percentage = float(input("Enter percentage you scored: "))

if percentage >= 90:
    print(f"{name}, you've got 'A' Grade")
elif percentage >= 80:
    print(f"{name}, you've got 'B' Grade")
elif percentage >= 70:
    print(f"{name}, you've got 'C' Grade")
elif percentage >= 60:
    print(f"{name}, you've got 'D' Grade")
else:
    print(f"{name}, you've got 'E' Grade")
