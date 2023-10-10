# first three characters must be uppercase random alphabets
# 4th place characters must be one of P C A F H T
# fifth place any random uppercase alphabet
# four digits
# one alphabet uppercase

from re import *

pan_num=input("enter the pancard number")

rule="[A-Z]{3}[PCAFHT]{1}[A-Z]{1}[\d]{4}[A-Z]{1}"

matcher=fullmatch(rule,pan_num)
print("invalid" if matcher==None else "valid")