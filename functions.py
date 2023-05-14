# use os to clear screen after displaying menu
from os import system, name

# to delay clearing so it looks smoother
from time import sleep

delay = 0.5
def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

# error checking function
def floatCheck(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
    

def calc():
    sleep(delay)
    clear()
    # ask user for input
    num1 = input("Please enter the first number: ")
  
    # error check
    if floatCheck(num1) == True:
      num1 = float(num1)
    else:
      print("That was not a valid input")
      sleep(delay)
      return
      
    opperation = input("Please enter an opperation from the following: +, -, *, / \n")
    
    num2 = input("Please enter the second number: ")
  
    # error check
    if floatCheck(num2) == True:
      num2 = float(num2)
    else:
      print("That was not a valid input")
      sleep(delay)
      return
      
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
        sleep(delay*2)
        return

    print(num1, opperation, num2, "=", ans)
    input("Press enter to continue...")

def conversion():
    sleep(delay)
    clear()
    """Kilos to Stone
- Gigabytes to bytes
- Inches to Centimetres
- Days to Seconds"""

    def kilo2stone(kilo):
        stone = kilo/6.35029
        print(kilo, "kg is", stone, "st\n")

    def stone2kilo(stone):
        kilo = stone * 6.35029
        print(kilo, "st is", stone, "kg\n")

    def gig2byte(gig):
        byte = gig * 10**9
        print(gig, "gigabytes are", byte, "bytes\n")
    
    def byte2gig(byte):
        gig = byte * 10**-9
        print(byte, "gigabytes are", gig, "bytes\n")

    def in2cm(inches):
      cm = inches * 2.54
      print(inches, "in are", cm, "cm\n")

    def cm2in(cm):
        inches = cm / 2.54
        print(cm, "cm are", inches, "in\n")

    def day2s(day):
        s = day * 24 * 60 * 60
        print(day, "days are", s, "seconds\n")
    
    def s2day(s):
        day = s/(24 * 60 * 60)
        print(s, "seconds are", day, "days\n")


    print("Enter 1 to convert kilos to stone\n" +
                "Enter 2 to covert stone to kilo\n"+
                "Enter 3 to convert gigabytes to bytes\n"+
                "Enter 4 to convert bytes to gigabytes\n"+
                "Enter 5 to convert inches to centimeters\n"+
                "Enter 6 to convert centimeters to inches\n"+
                "Enter 7 to convert days to seconds\n"+
                "Enter 8 to convert seconds to days\n")
    
    convert = input()
    if floatCheck(convert) == True:
      convert = float(convert)
    else:
      print("That was not a valid input")
      sleep(delay)
      return

    num = input("Please enter a number that you would like to convert: ")
    # error check
    if floatCheck(num) == True:
      num = float(num)
    else:
      print("That was not a valid input")
      sleep(delay)
      return
  
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
    else:
      print("That was not a valid input")
      sleep(delay)
      return
    input("Press enter to continue...")

# error check to be done
def convertBase():
  sleep(delay)
  clear()
  """
  Decimal, Binary, Octal and Hexadecimal.
  """
  # [2:] splits string so 0b is removed from the beginning
  def decimal2binary(decimal):
    return bin(decimal)[2:]
    
  def decimal2octal(decimal):
    return oct(decimal)[2:]
    
  def decimal2hex(decimal):
    return hex(decimal)[2:]
    
  def binary2dec(binary):
    # 2 tells the program to use decimal
    return int(binary, 2)
    
  def binary2octal(binary):
    decimal = binary2dec(binary)
    return decimal2octal(decimal)
    
  def binary2hex(binary):
    decimal = binary2dec(binary)
    return decimal2hex(decimal)
    
  def oct2dec(octal):
    return int(octal, 8)
    
  def oct2binary(octal):
    decimal = oct2dec(octal)
    return decimal2binary(decimal)
    
  def oct2hex(octal):
    decimal = oct2dec(octal)
    return decimal2hex(decimal)
    
  def hex2dec(hexadecimal):
    return int(hexadecimal, 16)
    
  def hex2binary(hexadecimal):
    decimal = hex2dec(hexadecimal)
    return decimal2binary(decimal)
    
  def hex2octal(hexadecimal):
    decimal = hex2dec(hexadecimal)
    return decimal2octal(decimal)

  def decimal():
    decimal = int(input("Enter a decimal number: "))
    binary = decimal2binary(decimal)
    octal = decimal2octal(decimal)
    hexadecimal = decimal2hex(decimal)
    print("Binary:", binary)
    print("Octal:", octal)
    print("Hexadecimal:", hexadecimal)
    
  def binary():
    binary = input("Enter a binary number: ")
    decimal = binary2dec(binary)
    octal = binary2octal(binary)
    hexadecimal = binary2hex(binary)
    print("Decimal:", decimal)
    print("Octal:", octal)
    print("Hexadecimal:", hexadecimal)
    
  def octal():
    octal = input("Enter an octal number: ")
    decimal = oct2dec(octal)
    binary = oct2binary(octal)
    hexadecimal = oct2hex(octal)
    print("Decimal:", decimal)
    print("Binary:", binary)
    print("Hexadecimal:", hexadecimal)
    
  def hexadecimal():
    hexadecimal = input("Enter a hexadecimal number: ")
    decimal = hex2dec(hexadecimal)
    binary = hex2binary(hexadecimal)
    octal = hex2octal(hexadecimal)
    print("Decimal:", decimal)
    print("Binary:", binary)
    print("Octal:", octal)
  
  print("Enter 1 to convert decimal to binary, octal, hexadecimal\n" +
        "Enter 2 to covert binary to decimal, octal, hexadecimal\n"+
        "Enter 3 to convert octal to decimal, binary, hexadecimal\n"+
        "Enter 4 to convert hexadecimal to decimal, binary, octal\n")
    
  convert = input()
  if floatCheck(convert) == True:
    convert = float(convert)
  else:
    print("That was not a valid input")
    sleep(delay)
    return

  if convert == 1:
    decimal()
  elif convert == 2:
    binary()
  elif convert == 3:
    octal()
  elif convert == 4:
    hexadecimal()
  else:
    print("That was not a valid input")
    sleep(delay)
    return
  input("Press enter to continue...")    
