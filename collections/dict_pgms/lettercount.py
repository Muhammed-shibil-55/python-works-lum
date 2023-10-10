text="carrot"
ch_count={}
for ch in text:
    if ch in ch_count:
        ch_count[ch]+=1
    else:
        ch_count[ch]=1
print(ch_count)