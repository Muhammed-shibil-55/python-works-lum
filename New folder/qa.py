lst=[
    [25,27,30],
    [33,35,39],
    [40,41,42],
    [70,72,73]
    ]
num=int(input("enter the number : "))
flag=False
for l in lst:
    upp=len(l)-1
    mid=upp-1
    if(l[mid] == num):
        print(f"{l[mid]} found")
        flag=True
    elif(l[mid-1]==num):
        print(f"{l[mid-1]} found")
        flag=True
    elif(l[mid+1]==num):
        print(f"{l[mid+1]} found")
        flag=True

if flag == False :
    print("not found")