# print words starting with vowels

stri=input("enter the sentence : ")
print("words starting with vowels=",end=" ")
words=stri.split(" ")
for w in words:
    for ch in w:
        if ch.casefold() in["a","e","i","u","o"]:
            print(w,",",end=" ")
            break
        else:
            break


# method using startswith()
# vowels=("a","e","i","u","o")
# for w in words:
#     if w.casefold().startswith(vowels):
#         print(w,",",end=" ")