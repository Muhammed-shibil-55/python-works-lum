num1=int(input("enter the first number : "))
num2=int(input("enter the second number :"))
# if(num1>num2):
#     les=num2
# else:
#     les=num1
# def lcm(l,n1,n2):
#     for i in range(1,l+1):
#         if(n1%i==0 and n2%i==0):
#             hcf=i
#     lcm=(num1*num2)/hcf
#     return lcm
# print("least common multiple=",lcm(les,num1,num2))


def least_cm(n1,n2):
    max=n1 if n1>n2 else n2
    flag=True
    while(flag):
        if(max%n1==0 and max%n2==0):
            print(f"lcm of {n1} and {n2} is {max}")
            break 
        else:
            max+=1
least_cm(num1,num2)