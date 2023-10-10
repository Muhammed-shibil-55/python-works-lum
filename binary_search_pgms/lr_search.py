lst=[10,12,14,16,18,20]
# linear search
element=16
i=0
stop=len(lst)
is_found=False
while(i<stop):
    cur_value=lst[i]
    if element==cur_value:
        is_found=True
        break
    i+=1
print(is_found)