from re import *

text="abaASDE235 @2saA"
# pattern="[a-zA-Z0-9]"
# pattern="[^0-9]" ^ used for excluding
# predefined characters
# pattern="\d" [0-9]
# pattern="\D" exclude digits
# pattern="\w" alpabets and numbers
# pattern="\W" special characters (excludes all alpabets and numbers)

pattern="\W"
matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())