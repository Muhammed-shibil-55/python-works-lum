# cases to check
# worst case
# edge case

lst=[11,22,13,15,17,16,10]
element=10
lst.sort()
low=0
upp=len(lst)-1
is_found=False

while(low<=upp):
    mid=(low+upp)//2
    if element==lst[mid]:
        is_found=True
        break
    elif element>lst[mid]:
        low=mid+1
    elif element<lst[mid]:
        upp=mid-1
        
print(is_found)