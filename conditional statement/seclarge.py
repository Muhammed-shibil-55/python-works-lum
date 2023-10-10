num1=int(input("enter number 1 : "))
num2=int(input("enter number 2 : "))
num3=int(input("enter number 3 : "))

if(num1==num2==num3):
    print("all numbers are equal")
elif(((num1>num2) and (num1<num3)) or ((num1<num2) and (num1>num3))):
    print("number1 is second largest number")
elif(((num2>num1) and (num2<num3)) or ((num2<num1) and (num2>num3))):
    print("number2 is seond largest")
elif(((num3>num2) and (num3<num1)) or ((num3<num2) and (num3>num1))):
    print("number3 is seond largest")