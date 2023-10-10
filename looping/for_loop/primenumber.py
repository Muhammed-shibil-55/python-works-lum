num=int(input("enter the number : "))
is_prime=True
for i in range(2,num):
    if(num%i==0):
        is_prime=False
        break
if(is_prime==True):
    print("prime number")
else:
    print("not prime number")
