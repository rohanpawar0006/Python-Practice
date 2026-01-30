n = int(input("Enter the value of N: "))
sum1 = 0
for i in range (1, n+1):
    i = 1/i**3
    sum1 = sum1 + i
print(sum1)
