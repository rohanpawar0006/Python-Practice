name = input("Enter the name of person for driving license: ")
age = int(input("Enter your age: "))
if age >= 18:
    print(f"{name} Eligible to apply for a driving license!")
else:
    temp = 18 - age
    year = 2026 + temp
    print(f"{name} not eligible to apply for a driving license, come in {year} to re-apply!")
