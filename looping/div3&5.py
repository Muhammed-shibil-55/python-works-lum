# print all numbers which are divisible by 3 and 5 upto given range
# start,end - user

strt=int(input("enter the starting number : "))
end=int(input("enter the ending number : "))
while(strt<=end):
    if(strt%3==0 and strt%5==0):
        print(strt)
    strt+=1