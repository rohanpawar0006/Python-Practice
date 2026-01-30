print("Welcome to festival discount deal!")
def festiveDiscount(totShopAmt, is_member):
    if totShopAmt >=500 and totShopAmt < 1000:
        discount = 5
    elif totShopAmt >=1000 and totShopAmt < 2000:
        discount = 8
    elif totShopAmt >= 2000:
        discount = 10
    else:
        discount = 0
    if is_member:
        discount += 5
    discount = totShopAmt*(discount/100)
    Net_Amount_Payable = totShopAmt - discount
    print("Your Total Amount after discount is: ", Net_Amount_Payable)

totShopAmt = float(input("Enter your Shopping Amount: "))
member = input("Are you a member of this store? type 'yes' or 'no': ")
is_member = True if member == 'yes' else False
festiveDiscount(totShopAmt, is_member)
