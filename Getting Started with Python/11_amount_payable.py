principal = int(input("Enter the Principal Amount: "))
rate_of_interest = float(input("Enter the Rate of Interest: "))
time = int(input("Entet the Time: "))
simple_interest = (principal*rate_of_interest*time)/100
amount_payable = principal + simple_interest
print(f"The Amount Payable is {amount_payable} for the Principal Amount of {principal} on Interest {simple_interest}")
