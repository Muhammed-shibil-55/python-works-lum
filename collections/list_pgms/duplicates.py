arr=[5,2,5,3,4,1,2,5,3,3]
arr.sort()
duplicate_list=[]
# print duplicates in arr
for a in range(0,len(arr)-1):
    curr=arr[a]
    next=arr[a+1]
    if curr==next:
        if curr not in duplicate_list:
            duplicate_list.append(curr)

for d in duplicate_list:
    print(d)

