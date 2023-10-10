# atleast 1 uppercase
# alteast 1 special character
# atleast 1 digit
# minimum 8 character

from re import *
pwd=input("enter the password : ")
rule="(?=.*[A-Z])(?=.*[\W_])(?=.*[\d]).{8,}"

matcher=fullmatch(rule,pwd)

print("invalid" if matcher==None else "valid")


# ?=. -> +ve lookout