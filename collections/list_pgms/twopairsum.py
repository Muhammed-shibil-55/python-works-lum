lst=[2,4,3,5]
sum=8
lst.sort()
low=0
upp=len(lst)-1
while(low<upp):
    cur_sum=lst[low]+lst[upp]
    if(cur_sum==sum):
        print(f"pairs are {lst[low]} and {lst[upp]}")
        break
    elif(cur_sum<sum):
        low+=1
    else:
        upp-=1
