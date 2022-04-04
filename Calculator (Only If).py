import math

ch = input("Enter the symbol of operation you want to perform :\nAddition (+)\nSubstraction (-)\nMultiplication (*)\nDivision (/)\nPower (^)\nSine (sin)\nCosine (cos) \nTangent(tan)\n")
if ch == '+':
    a = float(input("Enter 1st number :"))
    b = float(input("Enter 2nd number :"))
    print(a + b)

elif ch == '-':
    a = float(input("Enter 1st number :"))
    b = float(input("Enter 2nd number :"))
    print(a - b)

elif ch == '*':
    a = float(input("Enter 1st number :"))
    b = float(input("Enter 2nd number :"))
    print(a * b)

elif ch == '/':
    a = float(input("Enter 1st number :"))
    b = float(input("Enter 2nd number :"))
    print(a / b)

elif ch == '^':
    a = float(input("Enter base :"))
    b = float(input("Enter exponent :"))
    print(a ** b)
    
elif ch == 'sin':
    a = float(input("Enter the angle in radians :"))
    print(math.sin(a))

elif ch == 'cos':
    a = float(input("Enter the angle in radians :"))
    print(math.cos(a))

elif ch == 'tan':
    a = float(input("Enter the angle in radians :"))
    print(math.tan(a))

else:
    print("Operation NOT Supported!")
