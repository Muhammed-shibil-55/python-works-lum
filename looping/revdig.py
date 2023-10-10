num=int(input("enter the number : "))
dig=0
stri=" "
while(num!=0):
    dig=num%10
    stri+=str(dig)
    num=num//10
print(stri)