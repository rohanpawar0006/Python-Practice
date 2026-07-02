class Atm:
    #constrcutor(special function)
    def __init__(self):
        self.__pin = ""
        self.__balance = 0
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
        self.__pin = user_pin
        
        user_balance = int(input("Enter your balance: "))
        self.__balance = user_balance
        
        print("Pin Created Successfullty!")
        self.menu()
        
    def change_pin(self):
        old_pin = input("Enter your old pin")
        if old_pin == self.__pin:
            new_pin = input("Enter new pin: ")
            self.__pin = new_pin
            print("Pin Change Successfully!")
        else:
            print("Entered old pin is wrong :/")
        self.menu()
            
    def check_balance(self):
        user_pin = input("Enter your pin: ")
        if user_pin == self.__pin:
            print("Your Current Balance: ", self.__balance)
        else:
            print("You Entered Wrong Pin.")
        self.menu()
    def withdraw(self):
        user_pin = input("Enter your pin: ")
        if user_pin == self.__pin:
            amount = int(input("Enter the amount to withdrawal: "))
            if amount <= self.__balance:
                self.__balance -= amount
                print("Withdrawal successful is: ", amount)
                print("Balance: ", self.__balance)
            else:
                print("Insufficient Balance!")
        else:
            print("Enter correct pin.")
        self.menu()
obj = Atm()
obj.menu()


