from re import *

name=input("enter the variablename: ")
rule="[k-m][369][\w]*"

matcher=fullmatch(rule,name)

print("invalid" if matcher==None else "valid")

# rule
# firstplace=k...m
# secondplace= must be a digit that/3
# any number of characters