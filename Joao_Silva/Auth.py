import tic_tac_toe
import calculator

users = {}
LoggedUser = ""

# File Functions----------------------------------------------------------------
def writeToFile(string):
    file = open("UserFiles.txt", "a")
    file.write(string + "\n")
    file.close()

def writeStringToFile(file, string):
    file.write(string + "\n")

def readFromFile(target):
    file = open("UserFiles.txt", "r")
    for line in file.readlines():
        data = line.split(" ")
        if data[0] == target:
            return data[1].replace("\n", "")
    return ""

def readAllRegists():
    file = open("UserFiles.txt", "r")
    for line in file.readlines():
        data = line.split(" ")
        username = data[0]
        password = data[1].replace("\n", "")
        users[username] = password

#-------------------------------------------------------------------------------

# Encryption--------------------------------------------------------------------
def encrypt(password):
    return "".join(chr(126-ord(char)+33) for char in password)

def decrypt(password):
    return "".join(chr(126-ord(char)+33) for char in password)

#-------------------------------------------------------------------------------

def MainMenu():
    print("\n"*50)
    while True:
        option = input("1 - Login\n2 - Register\n3 - Exit\n")

        if option == "1":
            Login()
        elif option == "2":
            Register()
        elif option == "3":
            writeBackUserInfo()
            exit(0)
        else:
            print("No valid option selected")

def LoginMenu():
    while True:
        option = input("1 - Tic-Tac-Toe\n2 - Calculator\n3 - Chatbot\n4 - Change password\n5 - Logout\n")
        if option == "1":
            tic_tac_toe.play()
        elif option == "2":
            calculator.start()
        elif option == "3":
            pass
        elif option == "4":
            changePassword()
        elif option == "5":
            global LoggedUser
            LoggedUser = ""
            return
        else:
            print("No valid option selected")

# Function to register a user
# Note: Implement checking if user exists
def Register():
    username = input("Username: ")
    password = input("Password: ")

    if username in users.keys():
        print("Username already exists.")
        return

    forbidden_chars = [x for x in username if ord(x) < 33]
    if len(forbidden_chars) != 0:
        print("Forbidden char in username!")
        return

    encrypted_pass = encrypt(password)
    writeToFile(username + " " + encrypted_pass)

    users[username] = encrypted_pass

    print("Register successful")
    return


#Login function
def Login():
    global LoggedUser
    username = input("Username: ")
    password = input("Password: ")
    
    if username not in users.keys():
        print("Username not found!")
        return

    encrypted_password = users[username]
    registed_password = decrypt(encrypted_password)

    if registed_password == password:
        print("Logged in")
        LoggedUser = username
        LoginMenu()
        return
    
    print("Wrong password")

def changePassword():
    confirm_password = input("Confirm password: ")
    encrypted_password = users[LoggedUser]
    registed_password = decrypt(encrypted_password)
    if registed_password == confirm_password:
        new_password = input("New password: ")
        users[LoggedUser] = encrypt(new_password)
    else:
        print("Wrong password")

def writeBackUserInfo():
    file = open("UserFiles.txt", "w")
    for key in users.keys():
        writeStringToFile(file, key + " " + users[key])
    file.close()


if __name__ == "__main__":
    readAllRegists()
    MainMenu()

