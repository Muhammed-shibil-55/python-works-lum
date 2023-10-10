num=int(input("enter the number : "))
def fact(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i

    return fact
f=fact(num)
print(f"factorial of {num} = {f}")