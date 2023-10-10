#largest of three numbers

num1=int(input("enter number 1 : "))
num2=int(input("enter number 2 : "))
num3=int(input("enter number 3 : "))
if(num1==num2==num3):
    print("all numbers are equal")
elif(num1>num2 and num1>num3):
    print(f"{num1} is greater than two numbers")
elif(num2>num3):
    print(f"{num2} is greater than two numbers")
else:
    print(f"{num3} is greater than two numbers")

