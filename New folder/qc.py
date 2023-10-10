from re import *
text="ABCDABCDAB"
rule="[AB]"
matcher=finditer(rule,text)
for m in matcher:
    print(m.start(),m.group())