# decorators -> useed for reducing redundancies in the code

def swap_nums(fn):
    def wrapper(n1,n2):
        if n1<n2:
            (n1,n2)=(n2,n1)
        return fn(n1,n2)
    return wrapper

def smartdiv(fn):
    def wrapper(n1,n2):
        if n2==0:
            print("division by 0 is not possible")
            return
        return fn(n1,n2)
    return wrapper

@swap_nums
def sub(n1,n2):
    return n1-n2

@smartdiv
@swap_nums
def div(n1,n2):
    return n1/n2


print(sub(5,10))
print(div(5,0))
