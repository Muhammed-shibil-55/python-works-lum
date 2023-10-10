# films=["vigathakumaran","marthanda varma","balan","nirmala"]
# print("first film=",films[0])
# for f in films:
#     print(f)


expenses=[12000,13000,14000,11000,25000,28000,21000]

# print march month expenses
# print all expenses
# print costly expenses
# print expense > than 16000


print("expense of march",expenses[2])
print("all expenses:-")
for e in expenses:
  print(e)
# costly=0
# for e in expenses:
#     if(e>costly):
#         costly=e
# print("costly expense",costly)
# min_exp=expenses[0]
# for e in expenses:
#     if e<min_exp:
#         min_exp=e
# print("least expense",min)

print("expenses greater than 16000 :-")
for e in expenses:
    if(e>16000):
        print(e)
print("total expenses",sum(expenses))
print("maximum expense",max(expenses))
print("minimum expense",min(expenses))
srt=sorted(expenses)
rev_srt=sorted(expenses,reverse=True)
print("sorted expenses in ascending order",srt)
print("sorted expenses in descending order",rev_srt)