lst=[1,2,3,5,6,7]
curr=0
nxt=curr+1
if lst[0] !=1:
    print("first positive integer = 1")
for l in range(0,len(lst)-1):
    if((lst[nxt]-lst[curr]) !=1 ):
        print(f"first positive integer = {lst[curr]+1}")
        break
    else:
        curr+=1
        nxt+=1
