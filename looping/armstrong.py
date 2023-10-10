num=int(input("enter the number : "))
sum=0
temp=num
while(temp!=0):
    digit=temp%10
    cube=digit**3
    sum=sum+cube
    temp=temp//10
print("sum=",sum)
if(num==sum):
    print("number is armstrong")
else:
    print("not armstrong")
