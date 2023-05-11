import math
# use os to clear screen after displaying menu
from os import system, name
# to delay clearing so it looks smoother
from time import sleep

delay = 1
def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

def calc():
    sleep(delay)
    clear()
    # ask user for input
    num1 = float(input("Please enter the first number: "))
    opperation = input("Please enter an opperation from the following: +, -, *, / \n")
    num2 = float(input("Please enter the second number: "))

    # basic calculation
    if (opperation == "+"):
        ans = num1 + num2
    elif (opperation == "-"):
        ans = num1 - num2
    elif (opperation == "*"):
        ans = num1 * num2
    elif (opperation == "/"):
        ans = num1 / num2
    else:
        print("That was not a valid opperation")

    print(num1, opperation, num2, "=", ans)

def conversion():
    sleep(delay)
    clear()
    """Kilos to Stone
- Gigabytes to bytes
- Inches to Centimetres
- Days to Seconds"""

    def kilo2stone(kilo):
        stone = kilo/6.35029
        print(kilo, "kg is", stone, "st")

    def stone2kilo(stone):
        kilo = stone * 6.35029
        print(kilo, "st is", stone, "kg")

    def gig2byte(gig):
        byte = gig * 10**9
        print(gig, "gigabytes are", byte, "bytes")
    
    def byte2gig(byte):
        gig = byte * 10**-9
        print(byte, "gigabytes are", gig, "bytes")

    def in2cm(inches):
      cm = inches * 2.54
      print(inches, "in are", cm, "cm")

    def cm2in(cm):
        inches = cm /2.54
        print(cm, "cm are", inches, "in")

    def day2s(day):
        s = day * 24 * 60 * 60
        print(day, "days are", s, "seconds")
    
    def s2day(s):
        day = s/(24*60*60)
        print(s, "seconds are", day, "days")


    print("Enter 1 to convert kilos to stone\n" +
                "Enter 2 to covert stone to kilo\n"+
                "Enter 3 to convert gigabytes to bytes\n"+
                "Enter 4 to convert bytes to gigabytes\n"+
                "Enter 5 to convert inches to centimeters\n"+
                "Enter 6 to convert centimeters to inches\n"+
                "Enter 7 to convert days to seconds\n"+
                "Enter 8 to convert seconds to days\n")

    num = float(input("Please enter a number that you would like to convert: "))
 
    convert = int(input())

    if convert == 1:
        kilo2stone(num)
    elif convert == 2:
       stone2kilo(num)
    elif convert == 3:
       gig2byte(num)
    elif convert == 4:
       byte2gig(num)
    elif convert == 5:
       in2cm (num)
    elif convert == 6:
       cm2in (num)
    elif convert == 7:
       day2s(num)
    elif convert == 8:
       s2day(num)


repeat = True
while repeat:
    # ask user for conversion
    print("Enter 0 to close\n"+
                "Enter 1 for the normal calculator \n"+
                "Enter 2 for the conversion calculator")
    ahhh = int(input())
    sleep(delay )
    clear()
    if ahhh == 1:
        calc()
    elif ahhh == 2:
        conversion()
    else:
        repeat == False