lst1=[10,11,12,13,16]
lst2=[12,13,14,20,21]

# list common elements in two lists
for n  in lst1:
    if n in lst2:
        print(n)


#find alternate method
print("alternate method:-")
for l1 in lst1:
    for l2 in lst2:
        if l1==l2:
            print(l2)

# another alternate method
# for l in range(0,len(lst2)):
#     lst1.append(lst2[l])
# print(" another alternate method :-")
# print(lst1)
# lst1.sort()
# print(lst1)
# for a in range(0,len(lst1)-1):
#     curr=lst1[a]
#     next=lst1[a+1]
#     if(curr==next):
#         print(curr)

print(" another alternate method :-")
lst1.sort()
lst2.sort()
p1,p2=0,0
while(p1<len(lst1) and p2<len(lst2)):
    if(lst1[p1]==lst2[p2]):
        print("common element=",lst1[p1])
        p1+=1
    elif(lst1[p1]<lst2[p2]):
        p1+=1
    else:
        p2+=1
