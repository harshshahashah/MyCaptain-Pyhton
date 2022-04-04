import math

def add():
    a = float(input("Enter 1st number :"))
    b = float(input("Enter 2nd number :"))
    print(a + b)
    
def sub():
    a = float(input("Enter 1st number :"))
    b = float(input("Enter 2nd number :"))
    print(a - b)

def multi():
    a = float(input("Enter 1st number :"))
    b = float(input("Enter 2nd number :"))
    print(a * b)

def div():
    a = float(input("Enter 1st number :"))
    b = float(input("Enter 2nd number :"))
    print(a / b)

def pov():
    a = float(input("Enter base :"))
    b = float(input("Enter exponent :"))
    print(a ** b)

def sin():
    a = float(input("Enter the angle in radians :"))
    print(math.sin(a))

def cos():
    a = float(input("Enter the angle in radians :"))
    print(math.sin(a))
def tan():
    a = float(input("Enter the angle in radians :"))
    print(math.sin(a))

ch = input("Enter the symbol of operation you want to perform :\nAddition (+)\nSubstraction (-)\nMultiplication (*)\nDivision (/)\nPower (^)\nSine (sin)\nCosine (cos) \nTangent(tan)\n")


if ch == '+':
    add()

elif ch == '-':
    sub()

elif ch == '*':
    multi()

elif ch == '/':
    div()

elif ch == '^':
    pov()

elif ch == 'sin':
    sin()

elif ch == 'cos':
    cos()

elif ch == 'tan':
    tan()

else:
    print("Operation NOT Supported!")


    



