arr=[1,3,4,6,5]
# find least positive missing integer
arr.sort()
les=False
for a in range(0,len(arr)-1):
    curr=arr[a]
    next=arr[a+1]
    if arr[0]!=1:
        print("1 is missing")
        les=True
        break
    else:
      if(next-curr!=1):
        curr=curr+1
        print(f"least missing integer is {curr}")
        les=True
        break
if(les==False):
    print(f"least missing integer is {next+1}")
