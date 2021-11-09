# Hackerschool projet
# Francisco Carvalho
import Menus.user_menu as user_menu
import Menus.main_menu as main_menu
import apps.Calculator.menu as calc

import menuSelector

import loginSystem as logSys
################ Start of application ################
print("Hackerschool project")

# Define login system, singleton ?
loginSystem = logSys.LoginSystem()
selector = menuSelector.MenuSelector()

while True:
    if(not loginSystem.loggedIn):
        main_menu.printMainMenu(loginSystem)
    elif(selector.currentMenu == "USER"):
        user_menu.printUserMenu(loginSystem, selector)
    elif(selector.currentMenu == "CALCULATOR"):
        calc.print_calculator_menu(selector)
        