def printUserMenu(login_sys, selector):
    print("=====================================")
    print("1 - Change Password")
    print("2 - logout")
    print("3 - Calculator")
    print("=====================================")

    a = input()

    if a == "1":
        # Input
        newPassword = input("New passowrd: ")
        # Execute
        login_sys.changePassword(newPassword)
    elif a == "2":
        # Execute
        login_sys.logOut()

    elif a == "3":
        # Execute
        #calc.print_calculator_menu()
        login_sys.menuSelector = 1
        selector.currentMenu = "CALCULATOR"
    else:
        raise Exception("Command not found")