text="ABACDCE"

wc={}
dup_list=[]
for ch in text:
    if ch in wc:
        dup_list.append(ch)
    else:
        wc[ch]=1
print("second recursive chararcter :-",dup_list[1])


# method using list 
# non_list=[]
# dup_list=[]
# for ch in text:
#     if ch in non_list:
#         dup_list.append(ch)
#     else:
#         non_list.append(ch)
# print("second recursive chararcter :-",dup_list[1])