print(" Learning Exceptions...")

try:
    num1 = int(input("Enter the first number"))
    num2 = int(input("Enter the second number"))
    quotient = (num1 / num2)
    print("Both the numbers entered were correct")

except ValueError:             # to enter only integers
    print(" Please enter only numbers")

except ZeroDivisionError:      # Denominator should not be zero
    print(" Number 2 should not be zero")

else:
    print(" Great .. you are a good programmer")

finally:                       # to be executed at the end
    print(" JOB OVER... GO GET SOME REST")
