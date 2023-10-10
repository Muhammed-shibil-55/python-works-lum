from re import *
# starts with kl
# 2digit
# aphabet 0-2
# digit 4

vehicle_num=input("enter the number plate : ")
rule="(KL)-[\d]{2}-[A-Z]{0,2}-[\d]{4}"
matcher=fullmatch(rule,vehicle_num)

print("invalid" if matcher==None else "valid")