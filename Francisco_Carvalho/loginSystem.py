class LoginSystem:
    def __init__(self):
        self.currentUsername = ""
        self.loggedIn = False
        self.users = dict()


    def logOut(self):
        if(self.loggedIn):
            self.currentUsername = ""
            self.loggedIn = False
        else:
            raise Exception("Not logged in")

    def checkLogin(self,name, passowrd):
        if name in self.users:
            if self.users[name] == passowrd:
                return True
        return False

    def doRegisterUser(self,user,password):
        if user not in self.users:
            self.users[user] = password
        else:
            raise Exception("User \"{}\" already exists".format(user))

    def doLogin(self,name,password):
        if self.loggedIn:
            # ? - Should this be an exception?
            print("Already loged in")
        else:
            if self.checkLogin(name, password):
                self.currentUsername = name;
                self.loggedIn = True
                print("Hello "+self.currentUsername)
            else:
                print("Invalid username or password")

    def changePassword(self, pwd):
        # abstraction
        self.users[self.currentUsername] = pwd