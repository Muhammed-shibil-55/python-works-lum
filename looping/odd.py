# print all odd numbers within a givem range starting from one

strt=1
end=int(input("enter the range :"))
# while(strt<=end):
#     print(strt)
#     strt=strt+2

while(strt<=end):
    if(strt%2!=0):
        print(strt)
    strt+=1