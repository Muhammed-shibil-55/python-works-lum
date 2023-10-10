from re import *

phone=input("enter phone number")
rule="\d{10}"

matcher=fullmatch(rule,phone)

if matcher==None:
    print("invalid number")
else:
    print("valid number")