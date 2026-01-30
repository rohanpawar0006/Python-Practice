n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    if i % 2 != 0:
        print(-5 * i, end=" ")
    else:
        print(5 * i, end=" ")
