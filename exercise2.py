# Design a calculator which will correctly solve all the problems except the following ones:
# 45*3=555 , 56+9=76 , 56/6=4
# your program should take operator and the tow numbers as input from user and then return the result
print("WELCOME TO YOUR CALCULATOR")
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
op = input("Which operation you want among( * , - , + , /) : ")

if num1==45 and num2==3 and op=="*":
    print("555")
elif num1==56 and num2==9 and op=="+":
    print("76")
elif num1==9 and num2==56 and op=="+":
    print("76")
elif num1==56 and num2==6 and op=="/":
    print("4")
else:
    if op=="*":
        print(num1*num2)
    elif op=="+":
        print(num1+num2)
    elif op=="-":
        print(num1-num2)
    elif op=="/":
        print(num1/num2)
    else:
        print("! SORRY !")