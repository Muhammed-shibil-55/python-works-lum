celc=float(input("enter body temperature : "))
far=(celc*(9/5))+32
print("therm reading  :",far)
if(far>=99):
    print("person have fever")
else:
    print("normal temperature")