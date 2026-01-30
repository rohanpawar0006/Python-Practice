number = int(input("Enter a number: "))
print(f"Five numbers less than {number}:")
for i in range(1,6):
    mininum = number - i
    print(mininum)
print(f"Five numbers grater than {number}:")
for i in range(1,6):
    maximum = number + i
    print(maximum)

