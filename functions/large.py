num1=int(input("enter the first number : "))
num2=int(input("enter the second number : "))
num3=int(input("enter the third number : "))

def large(a,b,c):
    if(a>b and a>c):
        print(f"{a} is greatest")
    elif(b>c):
        print(f"{b} is greatest")
    else:
        print(f"{c} is greatest")

large(num1,num2,num3)