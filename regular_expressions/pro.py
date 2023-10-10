from re import *

f=open("C:\\Users\\shibi\\Desktop\\py_lum\\regular_expressions\\data.txt")
email=[]
phone_no=[]
phone_rule="\d{10}"
email_rule="[a-zA-Z]+[\w\W]*[@](gmail)[.]com"

for line in f:
    words=line.rstrip("\n").split(" ")
    for w in words:
        p_matcher=fullmatch(phone_rule,w)
        e_matcher=fullmatch(email_rule,w)
        if p_matcher != None:
            phone_no.append(w)
        elif e_matcher != None:
            email.append(w)
print(phone_no)
print(email)