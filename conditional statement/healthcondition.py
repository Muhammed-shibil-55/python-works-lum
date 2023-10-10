height_incm=int(input("enter the height in cm"))
weight_inkg=int(input("enter the weight in kg"))
height_inm=height_incm/100
bmi=weight_inkg//height_inm**2
print("body mass index = ",bmi)
if(bmi<20):
    print("underweight")
elif(bmi<25):
    print("normal weight")
elif(bmi<30):
    print("pre obesity")
else:
    print("obesity")        