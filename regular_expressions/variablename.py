from re import *
variable=input("enter the variable name")
rule="[a-zA-Z][\w_]*"

matcher=fullmatch(rule,variable)
print("invalid" if matcher==None else "valid")

