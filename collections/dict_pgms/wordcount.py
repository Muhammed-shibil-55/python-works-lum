txt="hello hi hello hi"
wrd=txt.split(" ")
wrd_count={}
for w in  wrd:
    if w in wrd_count:
        wrd_count[w]+=1
    else:
        wrd_count[w]=1

print(wrd_count)

