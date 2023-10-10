# alphabets and numbers
# @gmail.com

from re import *

id=input("enter the gmail id : ")
rule="[a-z0-9*]+[\W\w]*(@gmail.com)"

matcher=fullmatch(rule,id)

print("invalid" if matcher==None else "valid")

