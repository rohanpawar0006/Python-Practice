"""
Problem: Check if a Number is Prime
Goal
Write a function:
def is_prime(n):
That returns:
True if n is prime
False otherwise
Then:
Take input from user
Call the function
Print Prime or Not Prime
Constraints
n ≥ 1
Time complexity should be better than O(n)
👉 Hint: Think about √n
"""
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
number = int(input("Enter a number: "))
if is_prime(number) == True:
    print("Prime")
else:
    print("Not Prime")

""" 
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


Score: 8 / 10
Rubric:
Correctness: 10/10
Use of functions: 9/10
Time complexity awareness: 6/1
Interview readiness: 8/10
"""