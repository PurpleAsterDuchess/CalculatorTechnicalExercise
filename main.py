# get the code from functions.py
from functions import *

repeat = True
while repeat:
    # ask user for conversion
    clear()  
    print("Enter 0 to close\n"+
                "Enter 1 for the normal calculator \n"+
                "Enter 2 for the conversion calculator\n"+
                "Enter 3 for the base calculator")
    option = input()
    clear()
    if option == "0":
      repeat = False
    elif option =="1":
      calc()
    elif option == "2":
      conversion()
    elif option == "3":
      convertBase()
    else:
        print("That was not a valid input.")
        sleep(delay)
