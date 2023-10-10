# 3digit
# /
# 2didgitR
# 2digit
# /
# 2digit alphabet

from re import *

tyrecode=input("enter thr tyre code")
rule="[\d]{3}[/][\d]{2}[R]{1}[\d]{2}[/][\d]{2}[A-Z]{1}"

matcher=fullmatch(rule,tyrecode)
print("invalid" if matcher==None else "valid")