from re import *

text="goodmorning #shibil005"
# pattern="[aeiou]" # print all vowels from text using re
pattern="[^aeiou\W\d]" # print all consonants from text using re
matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())