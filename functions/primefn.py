num=int(input("enter the number : "))
def prime(n):
    f=0
    for i in range(2,num):
        if(n%i==0):
            f=1
            break
    return f
flag=prime(num)
if(flag==0):
    print("number is prime")
else:
    print("number is not prime")    
