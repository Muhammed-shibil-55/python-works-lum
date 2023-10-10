# find hcf using fn
# find lcm using fn
# check given num is prime or not
# define a fn that returns factorial of a number
num1=int(input("enter the first number : "))
num2=int(input("enter the second number :"))
if(num1>num2):
    les=num2
else:
    les=num1
def hcf(l,n1,n2):
    for i in range(1,l+1):
        if(n1%i==0 and n2%i==0):
            hcf=i
    return hcf
print("highest common factor=",hcf(les,num1,num2))
