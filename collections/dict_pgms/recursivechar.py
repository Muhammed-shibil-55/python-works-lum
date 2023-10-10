txt="ABCDAB"
ltrcont={}
for t in txt:
    if t in ltrcont:
        print("first recursive character=",t)
        break
    else:
        ltrcont[t]=1