class Atm:
    #constrcutor(special function)
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()
        
    def menu(self):
        user_input = int(input("""Hello How are you!,
            1. Press 1 to create pin.
            2. Press 2 for change pin.
            3. Press 3 to check balance
            4. Press 4 to withdraw
            5. Anything else to exit
            """))
        if user_input == 1:
            #create pin
            self.create_pin()
        elif user_input == 2:
            #change pin
            self.change_pin()
        elif user_input == 3:
            #check balance
            self.check_balance()
        elif user_input == 4:
            #withdraw
            self.withdraw()
        else:
            exit()
            
    def create_pin(self):
        user_pin = input("Enter your pin: ")
        self.pin = user_pin
        
        user_balance = int(input("Enter your balance: "))
        self.balance = user_balance
        
        print("Pin Created Successfullty!")
        self.menu()
        
    def change_pin(self):
        old_pin = input("Enter your old pin")
        if old_pin == self.pin:
            new_pin = input("Enter new pin: ")
            self.pin = new_pin
            print("Pin Change Successfully!")
            self.menu()
        else:
            print("Entered old pin is wrong :/")
        self.menu()
            
    def check_balance(self):
        user_pin = input("Enter your pin: ")
        if user_pin == self.pin:
            print("Your Current Balance: ", self.balance)
        else:
            print("You Entered Wrong Pin.")
            self.menu()
    def withdraw(self):
        user_pin = input("Enter your pin: ")
        if user_pin == self.pin:
            amount = int(input("Enter the amount to withdrawal: "))
            if amount <= self.balance:
                self.balance -= amount
                print("Withdrawal successful is: ", amount)
                print("Balance: ", self.balance)
            else:
                print("Insufficient Balance!")
        else:
            print("Enter correct pin.")
        self.menu()
obj = Atm()
obj.menu


