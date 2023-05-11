# get the code from calculator.py
from calculator import *

repeat = True
while repeat:
    # ask user for conversion
    clear()  
    print("Enter 0 to close\n"+
                "Enter 1 for the normal calculator \n"+
                "Enter 2 for the conversion calculator")
    option = int(input())
    clear()
    if option == 1:
        calc()
    elif option == 2:
        conversion()
    else:
        repeat = False
