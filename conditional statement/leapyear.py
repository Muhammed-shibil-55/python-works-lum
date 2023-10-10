#leap year or not
# case 1: if the year is a century it must be divisible by 400
# case2 : if year not century must be divisible by 4


yr=int(input("enter the year : "))
if(yr%100==0):
    if(yr%400==0):
        print("the year is leap year")
    else:
        print("the year is not leap year")
else:
    if(yr%4==0):
        print("the year is leap year")
    else:
        print("the year is not leap year")
    