#num=123
#1**3+2**3+3**3
#cube sum of digits

num=int(input("enter the number : "))
sum=0
while(num!=0):
    digit=num%10
    cube=digit**3
    sum=sum+cube
    num=num//10
print(f"cube sum of digits= {sum}")
