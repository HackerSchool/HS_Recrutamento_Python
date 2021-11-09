# This "module" contains all the menus
# This is the "view", the logic components should implement the funcions that
# could be called by the menu for IO operations

def printMainMenu(login_sys):
    # command descriptiom ------
    print("=====================================")
    print("1 - Login")
    print("2 - Register")
    print("3 - Exit")
    print("=====================================")
    
    a = input()
    
    # command execution --------
    if a == "2":
        # Input
        user = input("Username: ")
        passowrd = input("Password: ")
        # Execute
        try:
            login_sys.doRegisterUser(user, passowrd)
        except Exception as ex:
            print(str(ex))
    elif a == "1":
        # Input
        user = input("Username: ")
        password = input("Password: ")
        # Execute
        login_sys.doLogin(user,password)
    elif a == "3":
        exit()
    else:
        raise Exception("Command not found")