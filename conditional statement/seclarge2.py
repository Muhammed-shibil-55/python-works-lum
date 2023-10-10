num1=int(input("enter number 1 : "))
num2=int(input("enter number 2 : "))
num3=int(input("enter number 3 : "))
if(num1==num2==num3):
    print("all numbers are equal")
elif(num1>num2) and (num1>num3):
    if(num2>num3):
        print("number 2 is second largest")
    else:
        print("number 3 is second largest")
elif(num2>num3):
    if(num1>num3):
        print("number 1 is second largest")
    else:
        print("number 3 is second largest")
else:
    if(num1>num2):
        print("number 1 is second largest")
    else:
        print("number 2 is second largest")

