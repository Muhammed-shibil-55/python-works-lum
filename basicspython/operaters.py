# operaters
# 1.arithmetic=> +,-,*,/,%,**(exponential),//(floor division)
# 2.logical=> and or not
# 3.assignment=>
# 4.relational=> <,>,<=,>=,==,!=
# 5.bitwise=> & | ~
# 6.membership=>


#bitwise operaters
# &-and
print("bitwise and 1 and 2",1&2)  # 0001 &
            # 0010
            #=0000 = 0
# |-or
print("bitwise or 1 or 2",1|2) # 0001 |
           # 0010
           #=0011 = 3
# ~ -not
# positive not = opposite sign and increment 1
# negative not = opposite sign and decrement 1
print("bitwise not 1",~1)
print("bitwise not 2",~2)
print("bitwise not 3",~3)
print("bitwise not -1",~-1)
print("bitwise not -2",~-2)
print("bitwise not -3",~-3)


#membership operaters
# in,notin (string,list)=> outputs=>
name="shibil"
print("a" in name) #false
print("s" in name) #true
print("a" not in name) #true
print("s" not in name) #false