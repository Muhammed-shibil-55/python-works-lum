def decorator1(fn):
    def wrapper():
        print("this is before decorator 1 of originalfn")
        result=fn()
        print("this is after decorator 1 of originalfn")
        return
    return wrapper

def decorator2(fn):
    def wrapper():
        print("this is before decorator 2 of originalfn")
        result=fn()
        print("this is after decorator 2 of originalfn")
        return
    return wrapper


@decorator1
@decorator2
def origianlfunction():
    print("this is original function")

origianlfunction()