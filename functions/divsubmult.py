a=int(input("enter number : "))
b=int(input("enter a number : "))
 
def sub(x,y):
    sub=x-y
    print(f"{x}-{y}={sub}")

def mult(x,y):
    mul=x*y
    print(f"{x}*{y}={mul}")

def div(x,y):
    div=x/y
    print(f"{x}/{y}={div}")

sub(a,b)
mult(a,b)
div(a,b)