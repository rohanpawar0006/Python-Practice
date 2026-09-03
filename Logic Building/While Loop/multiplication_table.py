# 5. Print the multiplication table of a given number from n × 1 to n × 10. 
number = int(input("Enter the number for multiplication table: "))
n = 1
while n <= 10:
    print( number, "X" ,n, "=", number * n )
    n += 1