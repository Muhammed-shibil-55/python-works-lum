orders=["vegmeals","fishmeals","vegmeals","fishmeals","vb","cb","bb","vb","cb","bb","bb","vb","fried_rice"]
order_list={}
for item in orders:
    if item in order_list:
        order_list[item]+=1
    else:
        order_list[item]=1
print(order_list)