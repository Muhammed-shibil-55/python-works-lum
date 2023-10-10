def deccor1(fn):
    def wraapper():
        x=fn()
        return x*x
    return wraapper

def deccor2(fn):
    def wrapper():
        x=fn()
        return 2*x
    return wrapper


@deccor1
@deccor2
def num():
    return 10


print(num())