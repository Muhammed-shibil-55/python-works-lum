num=int(input("enter the number : "))
curr=1
prev=0
print(prev)
print(curr)
fib=0
for i in range(1,num+1):
    fib=curr+prev
    if(fib<=num):
        print(fib)
    prev=curr
    curr=fib
    