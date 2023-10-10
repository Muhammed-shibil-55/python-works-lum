num1=int(input("enter the first number : "))
num2=int(input("enter the second number : "))

#find hcf of two numbers
if(num1>num2):
    les=num1
else:
    les=num2
for i in range(les,1,-1):
    if(num1%i==0 and num2%i==0):
        hcf=i
        # break
print("highest common factor =",hcf)

# alternate method
# if(num1>num2):
#     les=num2
# else:
#     les=num1
# for i in range(1,les+1):
#     if(num1%i==0 and num2%i==0):
#         hcf=i
# print("highest common factor =",hcf)