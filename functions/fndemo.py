def add(n1,n2):
    res=n1+n2
    return res

print(add(30,40))


def cube(n):
    res=n**3
    return res

print(cube(3))


def max_two(n1,n2):
    if(n1>n2):
        stri=f"{n1} is greater"
    else:
        stri=f"{n2} is greater"
    return stri

print(max_two(10,12))


def sub(n1,n2):
    return n1-n2 
print(sub(12,6))

def smart_sub(n1,n2):
    if (n1>n2):
        return n1-n2
    else:
        return n2-n1
print(smart_sub(10,5))
print(smart_sub(5,10))

def oddeven(num):
    return f"{num} is even" if num%2==0 else f"{num} is odd"
print(oddeven(5))


def lcm(n1,n2):
    hcf=1
    les=n2 if n1>n2 else n1
    for i in range(1,les+1):
        if n1%i==0 and n2%i==0:
            hcf=i
    lcm=(n1*n2)/hcf
    return lcm
num1=int(input("enter the number : "))
num2=int(input("enter the number : "))
print(lcm(num1,num2))
