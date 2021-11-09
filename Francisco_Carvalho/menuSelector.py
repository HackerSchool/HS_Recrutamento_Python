class MenuSelector:
    def __init__(self):
        self.currentMenu = "USER"
    
    def goBack(self):
        if self.currentMenu == "CALCULATOR":
            self.currentMenu = "USER"