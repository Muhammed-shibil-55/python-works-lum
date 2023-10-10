text="ettayicoffee"
vow=0
cons=0
for ch in text:
    if ch in ["a","e","i","o","u"]:

        vow=vow+1
    else:
        cons=cons+1
print("number of vowels=",vow)
print("number of vowels=",cons)