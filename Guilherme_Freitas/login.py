from os import system
import math
from calc import *
def openfile():
    key_file=open("key.txt","r")
    #print(key_file.read())
    return key_file

def closefile(file):
    file.close()

def getInput():
    
    
    user=input("<user>")# a variavel 'user' serve como controlo para as diferentes opções que podem ser tomadas: mudar pass,novo utilizador,etc
    if(user=="logout"):
        exit() 
    elif(user=="r"):
        system("clear")
        new_user=input("<new username>")
        if(new_user=="e"):
            exit()
        new_key=input("<new password for({})>".format(new_user))
        key_file=open("key.txt","w")
        key_file.write("{}.{}\n".format(new_user,new_key))
        key_file.close()
        system("clear")
        print(">>changes written to file")
        getInput()
        #print("B-debug")
        return  new_user,new_key
    elif(user=="c"):
        renew_user=input("enter username for password change:")
        temp_key=input("enter current password for({}):".format(renew_user))
        renew_key=input("enter new password for ({}):".format(renew_user))
        key_file=open("key.txt","r")
        write_string=key_file.read()
        key_file.close()
        key_file=open("key.txt","w")
        leitura=write_string.replace(write_string,"")
        key_file.write(leitura)
        leitura=write_string.replace("{}.{}\n".format(renew_user,temp_key),"{}.{}\n".format(renew_user,renew_key))
        key_file.write(leitura)
        key_file.close()
            
        getInput()
        return renew_user,renew_key
        #return renew_key,renew_key
        
    elif(user!="r" or user !="e" or user !="c"): 
        key=input("<password for ({})>".format(user))
        #print("C-debug")
       
        return user,key

def doesInputMatch(a,b,file):
    check=0
    while(check==0):
        
        if "{}.{}\n".format(a,b) in file.read():
            print(">>user and password match")
            check=1
            system("clear")
            break
        else:
            check=0
            print("<<match not found>>")
            file=openfile()
            a,b=getInput()

            doesInputMatch(a,b,file)
            #print("debug")
            break
def app_menu():
    app=input(">1-calculator\n>2-not implemented,will exit\n>3-not implemented, will exit:\n")
    if(app=="1"):
        calc_init()
        while((calc())!=-1):
            calc()
        system("clear")
       # file=openfile()
        #user,key=getInput()
        #doesInputMatch(user,key,file)
        app_menu()
    elif(app=="2" or app=="3"):
        exit()
    elif(app=="return"):
        system("clear")
        file=openfile()
        user,key=getInput()
        doesInputMatch(user,key,file)
        app_menu()
                   


print("login screen            r to register new user     logout to exit")
file = openfile()
user,key=getInput()

doesInputMatch(user,key,file)
app_menu()

#print("debug")

    

    

