#HS Project
#from login import *
import math
from io import DEFAULT_BUFFER_SIZE, StringIO
from os import system
system("clear")
check=0 

def calc_init():
    system("clear")
    print("################################################################################")
    print("                                 CALCULATOR-type return to move back")
    print("################################################################################")
def calc():
    in_string=input(">")
    if(in_string=="return"):
        return -1
    

    #print("{}".format(in_string))
    operands=in_string.split()

    #print(operands[0],operands[1],operands[2])
    if(operands[1]=="+"):
        result=float(operands[0])+float(operands[2])
        print("={}".format(result))
    if(operands[1]=="-"):
        result=float(operands[0])-float(operands[2])
        print("={}".format(result))
    if(operands[1]=="*"):
        result=float(operands[0])*float(operands[2])
        print("={}".format(result))
    if(operands[1]=="/"):
        result=float(operands[0])/float(operands[2])
        print("={}".format(result))
    if(operands[1]=="**"):
        result=math.pow(float(operands[0]),float(operands[2]))
        print("={}".format(result))
    








    





