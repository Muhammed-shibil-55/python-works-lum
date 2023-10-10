low_lim=int(input("enter the lower limit : "))
up_lim=int(input("enter the upper limit : "))

for i in range(low_lim,up_lim+1):
    if(i%2==0):
        print(i)