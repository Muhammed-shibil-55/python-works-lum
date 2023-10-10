source_word="decreases"
target_word="dress"
flag=True

wc={}
for ch in source_word:
    if ch in wc:
        wc[ch]+=1
    else:
        wc[ch]=1

for ch in target_word:
    if ch in wc and wc.get(ch)>0:
        wc[ch]-=1
    else:
        flag=False
        break

print(flag)