def login(uid, pwd):
    if uid != "ADMIN":
        print("Invalid UserID!")
        return
    for attempt in range(3):
        if uid == "ADMIN" and pwd == "St0rE@1":
            print("Login Successful!")
            return
        else:
            remaining = 2 - attempt
            if remaining >= 0:
                print(f"Incorrect password. {remaining + 1} attempt(s) remaining.")
                pwd = input("Re-enter the Password: ")
    print("Account Blocked")
userid = input("Enter the UserID: ")
password = input("Enter the Password: ")
login(userid, password)
