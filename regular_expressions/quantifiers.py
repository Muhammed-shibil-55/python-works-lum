from re import *

text="aabbaaac"
# pattern="a+" # + -> one or more occurence of 'a'
# pattern="a*" #  * -> zero or more occurence of 'a'

pattern="a{1,2}" # -> minimum one occurence and maximum two occurence of a

matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())