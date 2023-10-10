source_word="chicken"
t_word="hen"
kangaroostr=""
source_w_list=[]
for ch in source_word:
    source_w_list.append(ch)
for ch in t_word:
    if ch in source_w_list:
        kangaroostr+=ch
        source_w_list.remove(ch)
    else:
        break
print(kangaroostr==t_word)
print("kangaroo" if kangaroostr==t_word else "not kw")
