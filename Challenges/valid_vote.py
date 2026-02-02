""" 
Problem: Valid Voting Age Checker
Goal
Write a Python program that:
Takes a person’s age as input 
Determines:
If the person is eligible to vote
Categorizes them as:
Child (age < 18)
Adult (18–59)
Senior Citizen (60+)
Inputs / Outputs
Input
One integer → age
Output
Line 1: Eligible to vote or Not eligible to vote
Line 2: Category (Child, Adult, Senior Citizen)
"""
print("-----------Valid Voting Age Checker-----------")
name = input("Enter Your Name: ")
age = int(input(f"{name} enter your age: "))

if age < 18:
    print(f"{name} not eligible to vote!")
    print("Your still Child, wait until you get 18+ years old!")
elif age < 60:
    print(f"{name} you are eligible to vote!")
    print("You're Adult")
else:
    print(f"{name} you are eligible to vote!")
    print("You're Senior Citizen")


""" 
age = int(input("Enter age: "))

if age < 18:
    print("Not eligible to vote")
    print("Child")
elif age < 60:
    print("Eligible to vote")
    print("Adult")
else:
    print("Eligible to vote")
    print("Senior Citizen")

"""
