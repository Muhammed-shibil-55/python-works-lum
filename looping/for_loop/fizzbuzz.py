#print all  numbers upto limit
# if number divisible by 3 print fizz if number divisible by 5 print buzz

# if divisible by 15 print fizzbuzz

low_lim=int(input("enter the lower limit : "))
up_lim=int(input("enter the upper limit :"))
for i in range(low_lim,up_lim+1):
    print(i,end="-")
    if(i%3==0):
        print("fizz")
    if(i%5==0):
        print("buzz")
    if(i%15==0):
        print("fizzbuzz")
    if((i%3!=0) and (i%5!=0) and (i%15!=0)):
        print("error")