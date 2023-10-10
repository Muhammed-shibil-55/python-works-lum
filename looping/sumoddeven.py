strt=int(input("enter the starting number :"))
range=int(input("enter the range: "))
sumodd=0
sumeven=0
while(strt<=range):
    if(strt%2==0):
        sumeven=sumeven+strt
    else:
        sumodd+=strt
    strt+=1
print("sum of all odd number upto range =",sumodd)
print("sum of all even numbers upto range=",sumeven)    