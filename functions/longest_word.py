text="hi hello hai goodafternoon"

words=text.split(" ")
l_word=max(words,key=lambda w:len(w))

print(l_word)

srt=sorted(words,reverse=True,key=lambda w:len(w))
print(srt)


lst_word=min(words,key=lambda w:len(w))
print(lst_word)